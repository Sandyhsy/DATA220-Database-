from PyQt5.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QPushButton, QMessageBox, QHeaderView
from PyQt5 import uic
import mysql.connector
from data201 import make_connection



class OrderWindow(QDialog):
    def __init__(self, main_window):
        super().__init__()
        uic.loadUi("customer_order_window.ui", self)

        # Store reference to MainWindow
        self.main_window = main_window

        # Access widgets
        self.table_orders = self.findChild(QTableWidget, "table_orders")
        self.table_order_details = self.findChild(QTableWidget, "table_order_details")
        self.cart_button = self.findChild(QPushButton, "pushButton")  # Back button

        # Set up tables
        self.setup_table(self.table_orders, ["Order ID", "Order Status", "Ordered Date", "Shipped Date", "Total"])
        self.setup_table(self.table_order_details, ["Product ID", "Product Name", "Unit Price", "Quantity", "Review"])

        # Connect Back button to go to MainWindow
        self.cart_button.clicked.connect(self.go_to_main_window)

        # Populate orders table by default
        self.populate_orders()

    def setup_table(self, table_widget, headers):
        """Set up table with non-adjustable headers."""
        table_widget.setColumnCount(len(headers))
        table_widget.setHorizontalHeaderLabels(headers)
        header = table_widget.horizontalHeader()

        # Fix header and prevent resizing
        header.setSectionsClickable(False)
        header.setStretchLastSection(False)  # Prevent last column from stretching

        # Set table properties
        table_widget.setEditTriggers(QTableWidget.NoEditTriggers)  # Make cells read-only
        table_widget.setWordWrap(True)  # Allow text wrapping in cells
        table_widget.setAlternatingRowColors(True)  # Alternate row colors

    def enforce_column_widths(self, table_widget):
        """Explicitly enforce larger column widths."""
        column_count = table_widget.columnCount()
        for i in range(column_count):
            if i == 2:  # "Ordered Date" column
                table_widget.setColumnWidth(i, 300)  # Wider for Ordered Date
            elif i == 3:  # "Shipped Date" column
                table_widget.setColumnWidth(i, 300)  # Wider for Shipped Date
            else:
                table_widget.setColumnWidth(i, 150)  # Larger default width for other columns
            header = table_widget.horizontalHeader()
            header.setSectionResizeMode(i, QHeaderView.Fixed)  # Enforce fixed mode


    def populate_orders(self):
        """Populate the orders table with data from the database."""
        try:

            conn = make_connection(config_file = 'sqlproject.ini')
            cursor = conn.cursor()  

            query = """
                SELECT 
                    oi.order_id,
                    o.order_status,
                    o.order_purchase_timestamp,
                    o.order_estimated_delivery_date,
                    SUM(op.payment_value) AS total
                FROM order_items oi
                JOIN orders o ON oi.order_id = o.order_id
                JOIN order_payments op ON o.order_id = op.order_id
                GROUP BY oi.order_id, o.order_status, o.order_purchase_timestamp, o.order_estimated_delivery_date
                ORDER BY o.order_purchase_timestamp DESC
            """
            cursor.execute(query)
            results = cursor.fetchall()

            self.table_orders.setRowCount(len(results))

            for row_index, row_data in enumerate(results):
                for col_index, value in enumerate(row_data):
                    self.table_orders.setItem(row_index, col_index, QTableWidgetItem(str(value)))

            # Apply initial resizing and enforce widths
            self.table_orders.resizeColumnsToContents()
            self.enforce_column_widths(self.table_orders)

            # Debug: Print column widths to confirm
            for i in range(self.table_orders.columnCount()):
                print(f"Column {i} width: {self.table_orders.columnWidth(i)}")

            # Connect cell click event to populate order details
            self.table_orders.cellClicked.connect(self.populate_order_details)

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Failed to retrieve orders: {err}")

    def populate_order_details(self, row, column):
        """Populate the order details table based on the selected order."""
        try:
            selected_order_id = self.table_orders.item(row, 0).text()
            conn = make_connection(config_file = 'sqlproject.ini')
            cursor = conn.cursor()  

            query = """
                SELECT 
                    oi.product_id,
                    p.product_description AS product_name,
                    p.product_price AS unit_price,
                    oi.quantity
                FROM order_items oi
                JOIN products p ON oi.product_id = p.product_id
                WHERE oi.order_id = %s
            """
            cursor.execute(query, (selected_order_id,))
            results = cursor.fetchall()

            self.table_order_details.setRowCount(len(results))

            for row_index, row_data in enumerate(results):
                for col_index, value in enumerate(row_data):
                    self.table_order_details.setItem(row_index, col_index, QTableWidgetItem(str(value)))

                # Add "Write Review" button in the last column
                review_button = QPushButton("Write Review")
                review_button.clicked.connect(
                    lambda _, p_id=row_data[0], p_name=row_data[1]: self.open_review_window(p_id, p_name)
                )
                self.table_order_details.setCellWidget(row_index, 4, review_button)

            # Apply initial resizing and enforce widths
            self.table_order_details.resizeColumnsToContents()
            self.enforce_column_widths(self.table_order_details)

            # Debug: Print column widths to confirm
            for i in range(self.table_order_details.columnCount()):
                print(f"Column {i} width: {self.table_order_details.columnWidth(i)}")

            cursor.close()
            conn.close()

        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Database Error", f"Failed to retrieve order details: {err}")

    def open_review_window(self, product_id, product_name):
        """Open the review window for the selected product."""
        from customer_review_window import ReviewWindow  # Import ReviewWindow here to avoid circular imports
        review_window = ReviewWindow(product_id, product_name)
        review_window.exec_()  # Show the review window as a modal dialog

    def go_to_main_window(self):
        """Return to MainWindow without closing."""
        self.hide()
        self.main_window.show()
