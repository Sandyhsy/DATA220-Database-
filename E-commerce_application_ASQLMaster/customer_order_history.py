from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem, QPushButton, QPlainTextEdit, QLabel, QComboBox, QMessageBox, QHeaderView, QLineEdit, QVBoxLayout, QWidget
from PyQt5 import uic
from data201 import make_connection
from data201 import make_connection
import mysql.connector



class ReviewWindow(QMainWindow):
    
    def __init__(self, product_id, product_name, order_window, order_id, customer_id):
        super().__init__()
        uic.loadUi("customer_review_window.ui", self)

        # Store customer_id
        self.customer_id = customer_id

        # Set background color
        self.setStyleSheet("background-color: #F8E7E7;")

        # Access widgets
        self.label_product_name = self.findChild(QLabel, "label_product_name")
        self.comboBox_rating = self.findChild(QComboBox, "comboBox_rating")
        self.plainTextEdit_review = self.findChild(QPlainTextEdit, "plainTextEdit_review")
        self.pushButton_submit = self.findChild(QPushButton, "pushButton_submit")

        # Initialize with product information
        self.product_id = product_id
        self.order_id = order_id  # Order associated with the review
        self.order_window = order_window  # Reference to the OrderWindow
        self.label_product_name.setText(f"Product: {product_name}")

        # Connect submit button
        self.pushButton_submit.clicked.connect(self.submit_review)

    def submit_review(self):
        try:
            # Get review details
            rating = self.comboBox_rating.currentText().split(" - ")[0]
            review_text = self.plainTextEdit_review.toPlainText()

            if not rating or not review_text.strip():
                QMessageBox.warning(self, "Incomplete Input", "Please fill out all fields before submitting.")
                return

            # Save the review to the order_reviews table
            conn = make_connection(config_file = 'sqlproject.ini')
            cursor = conn.cursor()  


            query = """
                INSERT INTO order_reviews (review_score, comment_message, review_date, order_id)
                VALUES (%s, %s, NOW(), %s)
            """
            cursor.execute(query, (rating, review_text, self.order_id))
            conn.commit()

            cursor.close()
            conn.close()

            # Show success message
            QMessageBox.information(self, "Review Submitted", "Thank you for your review!")

            # Refresh the order details in OrderWindow
            self.order_window.populate_order_details(
                self.order_window.table_orders.currentRow(), self.order_window.table_orders.currentColumn()
            )

            # Return to OrderWindow (order history)
            self.close()
            self.order_window.show()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Failed to submit the review: {err}")


class OrderWindow(QMainWindow):
    def __init__(self, main_window, customer_id):
        super().__init__()
        uic.loadUi("customer_order_window.ui", self)  # Correct UI for OrderWindow

        self.customer_id = customer_id
        self.main_window = main_window

        # Access widgets
        self.table_orders = self.findChild(QTableWidget, "table_orders")
        self.table_order_details = self.findChild(QTableWidget, "table_order_details")
        self.cart_button = self.findChild(QPushButton, "pushButton")  # Cart button

        # Add search box for filtering orders
        self.search_box = QLineEdit(self)
        self.search_box.setPlaceholderText("Search orders...")
        self.search_box.textChanged.connect(self.filter_orders)

        # Add the search box to the layout
        self.central_layout = QVBoxLayout()
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.central_layout.addWidget(self.search_box)
        self.central_layout.addWidget(self.table_orders)
        self.central_layout.addWidget(self.table_order_details)
        self.central_layout.addWidget(self.cart_button)
        self.central_widget.setLayout(self.central_layout)

        # Set up tables
        self.setup_table(self.table_orders, ["Order ID", "Order Status", "Ordered Date", "Shipped Date", "Total"])
        self.setup_table(self.table_order_details, [
            "Product ID", "Product Name", "Unit Price", "Quantity", "Review Score", "Review Comment", "Action"
        ])

        # Connect Cart button to go back to MainWindow
        self.cart_button.clicked.connect(self.go_to_main_window)

        # Populate orders table by default
        self.populate_orders()

    def setup_table(self, table_widget, headers):
        """Set up table with fixed column widths and non-adjustable headers."""
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)
        header = table_widget.horizontalHeader()

        # Prevent column resizing
        for i in range(len(headers)):
            header.setSectionResizeMode(i, QHeaderView.Fixed)

        # Set default column widths
        for i, column_name in enumerate(headers):
            if column_name in ["Ordered Date", "Shipped Date"]:
                table_widget.setColumnWidth(i, 300)  # Wider for date columns
            elif column_name == "Action":
                table_widget.setColumnWidth(i, 150)  # Action column width
            else:
                table_widget.setColumnWidth(i, 150)  # Default width for other columns

        # Disable editing and alternate row colors
        table_widget.setEditTriggers(QTableWidget.NoEditTriggers)
        table_widget.setAlternatingRowColors(True)

    def populate_orders(self):
        """Populate the orders table with data from the database."""
        try:
            # Establish the database connection
            conn = make_connection(config_file='sqlproject.ini')
            cursor = conn.cursor()

            # Query to fetch orders based on the customer_id
            query = """
                SELECT 
                    o.order_id,
                    o.order_status,
                    o.order_purchase_timestamp,
                    o.order_estimated_delivery_date,
                    COALESCE(SUM(op.payment_value), 0) AS total
                FROM order_items oi
                JOIN orders o ON oi.order_id = o.order_id
                LEFT JOIN order_payments op ON o.order_id = op.order_id
                WHERE o.customer_id = %s
                GROUP BY 
                    o.order_id, 
                    o.order_status, 
                    o.order_purchase_timestamp, 
                    o.order_estimated_delivery_date
                ORDER BY o.order_purchase_timestamp DESC
            """

            # Execute the query with the provided customer_id
            print(f"Fetching orders for customer_id: {self.customer_id}")
            cursor.execute(query, (self.customer_id,))
            self.orders_data = cursor.fetchall()

            print(f"Orders fetched: {self.orders_data}")

            # Clear the table and populate it with fetched data
            self.table_orders.setRowCount(0)
            if not self.orders_data:
                # Handle the case where no orders are found
                QMessageBox.information(self, "No Orders", "You have no order history.")
                return

            for row_index, row_data in enumerate(self.orders_data):
                self.table_orders.insertRow(row_index)
                for col_index, value in enumerate(row_data):
                    self.table_orders.setItem(row_index, col_index, QTableWidgetItem(str(value)))

            # Connect cell click event to populate order details
            self.table_orders.cellClicked.connect(self.populate_order_details)

            # Close the cursor and connection
            cursor.close()
            conn.close()

            print("Order history populated successfully.")

        except mysql.connector.Error as err:
            # Log and display database errors
            print(f"Database error: {err}")
            QMessageBox.critical(self, "Database Error", f"Failed to fetch orders: {err}")

        except Exception as e:
            # Handle unexpected errors
            print(f"Unexpected error: {e}")
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")


    def filter_orders(self):
        """Filter orders based on search input."""
        search_term = self.search_box.text().lower()
        self.table_orders.setRowCount(0)  # Clear the table

        # Filter the orders data
        filtered_data = [
            row for row in self.orders_data if any(search_term in str(cell).lower() for cell in row)
        ]

        # Populate the table with filtered data
        for row_index, row_data in enumerate(filtered_data):
            self.table_orders.insertRow(row_index)
            for col_index, value in enumerate(row_data):
                self.table_orders.setItem(row_index, col_index, QTableWidgetItem(str(value)))
    def closeEvent(self, event):
        """Override close event to return to main window."""
        if self.main_window:
            self.main_window.show()
        print("Order history closed, returning to main window.")
        event.accept()

    def populate_order_details(self, row, column):
        try:
            # Get the selected order ID
            selected_order_id = self.table_orders.item(row, 0).text()

            # --- Fetch product details ---
            product_results = []
            try:
                conn_products = make_connection(config_file='sqlproject.ini')
                cursor_products = conn_products.cursor()

                query_products = """
                    SELECT 
                        oi.product_id,
                        p.product_description AS product_name,
                        p.product_price AS unit_price,
                        oi.quantity
                    FROM 
                        order_items oi
                    JOIN 
                        products p ON oi.product_id = p.product_id
                    WHERE 
                        oi.order_id = %s
                """
                cursor_products.execute(query_products, (selected_order_id,))
                product_results = cursor_products.fetchall()

                # Ensure all results are consumed
                while cursor_products.nextset():
                    pass

            finally:
                cursor_products.close()
                conn_products.close()

            # --- Fetch review details ---
            review_results = []
            try:
                conn_review = make_connection(config_file='sqlproject.ini')
                cursor_review = conn_review.cursor()

                query_review = """
                    SELECT 
                        COALESCE(orv.review_score, 'No Review') AS review_score,
                        COALESCE(orv.comment_message, 'No Comments') AS review_comment
                    FROM 
                        order_reviews orv
                    WHERE 
                        orv.order_id = %s
                """
                cursor_review.execute(query_review, (selected_order_id,))
                review_results = cursor_review.fetchall()

                # Ensure all results are consumed
                while cursor_review.nextset():
                    pass

            finally:
                cursor_review.close()
                conn_review.close()

            # --- Populate the order details table ---
            self.table_order_details.setRowCount(0)  # Clear existing rows

            for row_index, product_data in enumerate(product_results):
                self.table_order_details.insertRow(row_index)
                for col_index, value in enumerate(product_data):
                    self.table_order_details.setItem(row_index, col_index, QTableWidgetItem(str(value)))

                # Add review score and comment if available
                review_score = "No Review"
                review_comment = "No Comments"

                if review_results:
                    review_score = review_results[0][0]
                    review_comment = review_results[0][1]

                self.table_order_details.setItem(row_index, 4, QTableWidgetItem(review_score))  # Review Score
                self.table_order_details.setItem(row_index, 5, QTableWidgetItem(review_comment))  # Review Comment

                # Add "Write a Review" button
                write_review_button = QPushButton("Write a Review")
                write_review_button.clicked.connect(
                    lambda _, p_id=product_data[0], p_name=product_data[1]: self.open_review_window(p_id, p_name, selected_order_id)
                )
                self.table_order_details.setCellWidget(row_index, 6, write_review_button)

        except mysql.connector.Error as err:
            print(f"Database error: {err}")
            QMessageBox.critical(self, "Database Error", f"Error fetching order details: {err}")

        except Exception as e:
            print(f"Unexpected error: {e}")
            QMessageBox.critical(self, "Error", f"Unexpected error occurred: {e}")


    def open_review_window(self, product_id, product_name, order_id):
        """Open the ReviewWindow for the selected product."""
        self.review_window = ReviewWindow(product_id, product_name, self, order_id, self.customer_id)
        self.review_window.show()
        self.hide()  # Hide the OrderWindow while the ReviewWindow is open

    def go_to_main_window(self):
        """Navigate back to the MainWindow."""
        self.close()
        self.main_window.show()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    from customer_home import CustomerHome
    main_window = CustomerHome()
    order_window = OrderWindow(main_window)
    order_window.show()
    sys.exit(app.exec_())
