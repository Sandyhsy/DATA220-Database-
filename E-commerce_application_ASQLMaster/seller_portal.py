import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QHeaderView, QMessageBox
from PyQt5.uic import loadUi
import mysql.connector
from data201 import make_connection
from shared import open_login_portal
class SellerPortal(QMainWindow):

    
    def __init__(self):
        super().__init__()
        loadUi("seller_portal.ui", self)

        # Default to the "Orders" page
        self.EmployeePortalStacked.setCurrentIndex(0)

        # Setup navigation for QStackedWidget
        self.setup_navigation()

        # Load initial data
        self.load_orders_data()
        self.load_customers_data()
        self.load_payments_data()

        # Setup tables with fixed column sizes
        self.setup_table(self.tblPg1Orders_4, [
            ("ID", 50),
            ("Status", 100),
            ("Ordered Date", 190),
            ("Order Approved Date", 190),
            ("Carrier Delivery Date", 200),
            ("Customer Delivery Date", 200),
            ("Estimated Delivery Date", 200)
        ])
        self.setup_table(self.tblPg1OrderDetails_4, [
            ("Product ID", 160),
            ("Product Category", 270),
            ("Product Name", 300),
            ("Product Price", 209),
            ("Quantity", 210),
        ])
        self.setup_table(self.tblCustomers_3, [
            ("Customer ID", 100),
            ("First Name", 150),
            ("Last Name", 150),
            ("Email", 300),
            ("Phone Number", 150),
            ("Zip-Code", 100)
        ])
        self.setup_table(self.tblPaymentsDetails_7, [
            ("Order ID", 100),
            ("First Name", 100),
            ("Last Name", 100),
            ("Customer ID", 100),
            ("Payment Type", 150),
            ("Installments", 150),
            ("Payment Value", 150)
        ])
        self.setup_table(self.tblOrderItems_7, [
            ("Order ID", 100),
            ("Product Category", 200),
            ("Product Description", 250),
            ("Quantity", 100),
            ("Price", 150),
            ("Order Date", 200)
        ])

        # Populate ComboBoxes
        self.populate_order_status_combobox()
        self.populate_payment_types()

        # Connect table row clicks to corresponding functions
        self.tblPg1Orders_4.cellClicked.connect(self.load_order_details)
        self.tblCustomers_3.cellClicked.connect(self.load_customer_order_details)
        self.tblPaymentsDetails_7.cellClicked.connect(self.load_order_items_from_payment)

        # Connect search and clear buttons
        self.btnCustSearch_4.clicked.connect(self.search_customers)
        self.btnCustSearch_5.clicked.connect(self.clear_search)
        self.btnCustSearch_6.clicked.connect(self.search_payments)
        self.btnCustSearch_7.clicked.connect(self.clear_payment_search)

        self.button_search_order_1.clicked.connect(self.search_orders)
        self.clear_all_order_search_1.clicked.connect(self.clear_all_order_search)
        self.populate_product_categories()
        self.populate_order_status()
        self.tblPg1Orders_4.cellClicked.connect(self.load_order_details)
        self.BtnDeleteCustomer_3.clicked.connect(self.delete_customer)
        self.BtnOrderDelay.clicked.connect(self.delay_order)
        self.BtnShipOrder.clicked.connect(self.ship_order)


    def populate_product_categories(self):
        """Populate the ComboBox with unique product categories."""
        connection = make_connection(config_file='sqlproject.ini')

        cursor = connection.cursor()

        query = "SELECT DISTINCT product_category FROM products"
        cursor.execute(query)
        categories = cursor.fetchall()

        self.ComboBox_product_category.addItem("All")  # Default option to show all categories
        for category in categories:
            self.ComboBox_product_category.addItem(category[0])

        cursor.close()
        connection.close()

    def populate_order_status_combobox(self):
        """Populate the order status ComboBox."""
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()

        query = "SELECT DISTINCT order_status FROM orders"
        cursor.execute(query)
        statuses = cursor.fetchall()

        self.ComboBox_status_order.addItem("")
        for status in statuses:
            self.ComboBox_status_order.addItem(status[0])

        cursor.close()
        connection.close()
    
    def setup_table(self, table_widget, columns):
        """Setup table headers and adjust column sizes."""
        header = table_widget.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Fixed)
        header.setStretchLastSection(False)
        header.setSectionsClickable(False)

        table_widget.setColumnCount(len(columns))
        headers, widths = zip(*columns)
        table_widget.setHorizontalHeaderLabels(headers)
        for idx, width in enumerate(widths):
            table_widget.setColumnWidth(idx, width)

    # === Orders Functionality ===
    def load_orders_data(self):
        """Load orders data into tblPg1Orders_4."""
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()

        query = """
        SELECT 
            order_id, order_status, order_purchase_timestamp, order_approved_at, 
            order_delivered_carrier_date, order_delivered_customer_date, 
            order_estimated_delivery_date
        FROM orders
        """
        cursor.execute(query)
        results = cursor.fetchall()

        self.tblPg1Orders_4.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tblPg1Orders_4.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        cursor.close()
        connection.close()

    
    def load_order_details(self, row, column):
        """Load order details into tblPg1OrderDetails_4."""
        order_id = self.tblPg1Orders_4.item(row, 0).text()
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()

        query = """
        SELECT 
            oi.product_id, p.product_category, p.product_description, 
            CONCAT('$', p.product_price), oi.quantity
        FROM order_items oi
        JOIN products p ON oi.product_id = p.product_id
        WHERE oi.order_id = %s
        """
        cursor.execute(query, (order_id,))
        results = cursor.fetchall()

        self.tblPg1OrderDetails_4.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tblPg1OrderDetails_4.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        cursor.close()
        connection.close()

    def populate_payment_types(self):
        """Populate the payment types ComboBox."""
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()

        query = "SELECT DISTINCT payment_type FROM order_payments"
        cursor.execute(query)
        payment_types = cursor.fetchall()

        self.comboBox.addItem("All")
        for payment_type in payment_types:
            self.comboBox.addItem(payment_type[0])

        cursor.close()
        connection.close()
        
    def search_orders(self):
        """Search orders based on Order ID, Product Category, and Order Status."""
        order_id = self.txtSrchOrderID_12.text().strip()  # Text input for Order ID
        product_category = self.ComboBox_product_category.currentText().strip()  # ComboBox for Product Category
        order_status = self.ComboBox_status_order_2.currentText().strip()  # ComboBox for Order Status

        # Base query to search for orders
        query = """
        SELECT 
            o.order_id, o.order_status, o.order_purchase_timestamp, 
            o.order_approved_at, o.order_delivered_carrier_date, 
            o.order_delivered_customer_date, o.order_estimated_delivery_date
        FROM orders o
        LEFT JOIN order_items oi ON o.order_id = oi.order_id
        LEFT JOIN products p ON oi.product_id = p.product_id
        WHERE 1=1
        """
        params = []

        # Add filters based on user input
        if order_id:
            query += " AND o.order_id = %s"
            params.append(order_id)
        if product_category and product_category != "All":
            query += " AND p.product_category = %s"
            params.append(product_category)
        if order_status and order_status != "All":
            query += " AND o.order_status = %s"
            params.append(order_status)

        # Connect to the database and execute the query
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Update the Orders table with the search results
        self.tblPg1Orders_4.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tblPg1Orders_4.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        cursor.close()
        connection.close()

    def clear_all_order_search(self):
        """Clear all search inputs and reload the orders table."""
        self.txtSrchOrderID_12.clear()  # Clear the Order ID search field
        self.ComboBox_product_category.setCurrentIndex(0)  # Reset Product Category ComboBox
        self.ComboBox_status_order_2.setCurrentIndex(0)  # Reset Order Status ComboBox
        self.load_orders_data()  # Reload the full orders table

    def populate_product_categories(self):
        """Populate the Product Category ComboBox."""
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()

        query = "SELECT DISTINCT product_category FROM products"
        cursor.execute(query)
        categories = cursor.fetchall()

        self.ComboBox_product_category.addItem("All")  # Default option to show all categories
        for category in categories:
            self.ComboBox_product_category.addItem(category[0])

        cursor.close()
        connection.close()

    def populate_order_status(self):
        """Populate the Order Status ComboBox."""
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()

        query = "SELECT DISTINCT order_status FROM orders"
        cursor.execute(query)
        statuses = cursor.fetchall()

        self.ComboBox_status_order_2.addItem("All")  # Default option to show all statuses
        for status in statuses:
            self.ComboBox_status_order_2.addItem(status[0])

        cursor.close()
        connection.close()

    # === Customers Functionality ===
    def load_customers_data(self):
        """Load customers data into tblCustomers_3."""
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()

        query = """
        SELECT DISTINCT customer_id, customer_first_name, customer_last_name, customer_email, 
            customer_phone, customer_zip_code
        FROM customers
        """
        cursor.execute(query)
        results = cursor.fetchall()

        self.tblCustomers_3.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tblCustomers_3.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        cursor.close()
        connection.close()

    def load_customer_order_details(self, row, column):
        """Load customer order details into tblCustOrders_3."""
        customer_id = self.tblCustomers_3.item(row, 0).text()
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()

        query = """
        SELECT 
            o.order_id, o.order_status, o.order_purchase_timestamp, 
            o.order_approved_at, o.order_delivered_carrier_date, 
            o.order_delivered_customer_date, o.order_estimated_delivery_date,
            SUM(oi.quantity) AS total_quantity
        FROM orders o
        LEFT JOIN order_items oi ON o.order_id = oi.order_id
        WHERE o.customer_id = %s
        GROUP BY o.order_id
        """
        cursor.execute(query, (customer_id,))
        results = cursor.fetchall()

        self.tblCustOrders_3.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tblCustOrders_3.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        cursor.close()
        connection.close()

    def load_payments_data(self):
        """Load payment details into tblPaymentsDetails_7."""
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()

        # Query to join customers, orders, and order_payments tables
        query = """
            SELECT 
                op.order_id,             -- Now the first column
                c.customer_first_name, 
                c.customer_last_name, 
                c.customer_id,           -- Switched position with `op.order_id`
                op.payment_type, 
                op.payment_installments,
                CONCAT('$', FORMAT(op.payment_value, 2)) AS payment_value
            FROM 
                customers c
            JOIN 
                orders o ON c.customer_id = o.customer_id
            JOIN 
                order_payments op ON o.order_id = op.order_id
        """
        cursor.execute(query)
        results = cursor.fetchall()

        # Set the row count for tblPaymentsDetails_7
        self.tblPaymentsDetails_7.setRowCount(len(results))

        # Populate the table with results
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tblPaymentsDetails_7.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        cursor.close()
        connection.close()


    def load_order_items_from_payment(self, row, column):
        """Load order items related to a payment into tblOrderItems_7."""
        try:
            # Get the Order ID from the selected row in tblPaymentsDetails_7
            order_id = self.tblPaymentsDetails_7.item(row, 0).text()  # Adjust column index as needed

            # Establish database connection
            connection = make_connection(config_file='sqlproject.ini')
            cursor = connection.cursor()

            # SQL query to get order items for the selected order
            query = """
            SELECT 
                oi.order_id,
                p.product_category,
                p.product_description,
                oi.quantity,
                CONCAT('$', FORMAT(p.product_price, 2)),
                o.order_purchase_timestamp
            FROM order_items oi
            JOIN products p ON oi.product_id = p.product_id
            JOIN orders o ON oi.order_id = o.order_id
            WHERE oi.order_id = %s
            """
            cursor.execute(query, (order_id,))
            results = cursor.fetchall()

            # Check if any results are returned
            if not results:
                self.tblOrderItems_7.setRowCount(0)  # Clear the table
                return

            # Set row count for the order items table
            self.tblOrderItems_7.setRowCount(len(results))

            # Populate the table with results
            for row_idx, row_data in enumerate(results):
                for col_idx, col_data in enumerate(row_data):
                    self.tblOrderItems_7.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

            cursor.close()
            connection.close()
        except Exception as e:
            print(f"Error loading order items: {e}")

    def search_customers(self):
        """Search for customers based on criteria."""
        customer_id = self.txtCustId_4.text().strip()
        first_name = self.txtSrchCustName_5.text().strip()
        last_name = self.txtSrchCustName_4.text().strip()
        order_status = self.ComboBox_status_order.currentText().strip()

        query = """
        SELECT 
            c.customer_id, c.customer_first_name, c.customer_last_name, c.customer_email, 
            c.customer_phone, c.customer_zip_code
        FROM customers c
        LEFT JOIN orders o ON c.customer_id = o.customer_id
        WHERE 1=1
        """
        params = []
        if customer_id:
            query += " AND c.customer_id = %s"
            params.append(customer_id)
        if first_name:
            query += " AND c.customer_first_name LIKE %s"
            params.append(f"%{first_name}%")
        if last_name:
            query += " AND c.customer_last_name LIKE %s"
            params.append(f"%{last_name}%")
        if order_status:
            query += " AND o.order_status = %s"
            params.append(order_status)

        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()

        self.tblCustomers_3.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tblCustomers_3.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        cursor.close()
        connection.close()

    def search_payments(self):
        """Search for payments based on Order ID, Payment Type, First Name, and Last Name."""
        # Retrieve search input from the UI elements
        order_id = self.txtSrchOrderID_11.text().strip()
        payment_type = self.comboBox.currentText().strip()
        first_name = self.txtSrchCustName_6.text().strip()
        last_name = self.txtSrchCustName_7.text().strip()

        # Base SQL query
        query = """
            SELECT op.order_id, c.customer_first_name, c.customer_last_name, c.customer_id, op.payment_type, op.payment_installments, CONCAT('$', FORMAT(op.payment_value, 2)) AS payment_value
            FROM customers c
            JOIN orders o ON c.customer_id = o.customer_id
            JOIN order_payments op ON o.order_id = op.order_id
            WHERE 1=1
        """
        params = []

        # Dynamically add filters based on input
        if order_id:
            query += " AND op.order_id = %s"
            params.append(order_id)
        if payment_type and payment_type != "All":  # Skip filtering if "All" is selected
            query += " AND op.payment_type = %s"
            params.append(payment_type)
        if first_name:
            query += " AND c.customer_first_name LIKE %s"
            params.append(f"%{first_name}%")
        if last_name:
            query += " AND c.customer_last_name LIKE %s"
            params.append(f"%{last_name}%")

        # Execute the query and populate the Payment Details table
        connection = make_connection(config_file='sqlproject.ini')
        cursor = connection.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()

        # Update the Payment Details table
        self.tblPaymentsDetails_7.setRowCount(len(results))
        for row_idx, row_data in enumerate(results):
            for col_idx, col_data in enumerate(row_data):
                self.tblPaymentsDetails_7.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        cursor.close()
        connection.close()

    def ship_order(self):
        """Change the order status from 'In Progress' to 'On the way'."""
        # Get the currently selected row in the tblPg1Orders_4 table
        current_row = self.tblPg1Orders_4.currentRow()

        if current_row < 0:
            # No row is selected
            QMessageBox.warning(self, "No Selection", "Please select an order to ship.")
            return

        # Get the Order ID and Status from the selected row
        order_id_item = self.tblPg1Orders_4.item(current_row, 0)
        order_status_item = self.tblPg1Orders_4.item(current_row, 1)

        if not order_id_item or not order_status_item:
            QMessageBox.warning(self, "Error", "Could not retrieve Order ID or Status.")
            return

        order_id = order_id_item.text()
        order_status = order_status_item.text()

        # Only proceed if the status is "In Progress"
        if order_status != "in progress":
            QMessageBox.warning(self, "Invalid Status", "Only orders with status 'In Progress' can be shipped.")
            return

        try:
            # Establish database connection
            connection = make_connection(config_file='sqlproject.ini')
            cursor = connection.cursor()

            # SQL query to update the order status
            update_query = """
            UPDATE orders
            SET order_status = 'On the way'
            WHERE order_id = %s AND order_status = 'In Progress'
            """
            cursor.execute(update_query, (order_id,))

            # Commit the changes
            connection.commit()

            # Refresh the table
            self.load_orders_data()

            QMessageBox.information(self, "Success", f"Order {order_id} status updated to 'On the way'.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to update order status: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        self.BtnShipOrder.clicked.connect(self.ship_order)

    def delay_order(self):
        """Change the status of a selected order from 'In Progress' to 'Order Delayed'."""
        # Get the currently selected row in the orders table
        current_row = self.tblPg1Orders_4.currentRow()
        
        if current_row < 0:
            QMessageBox.warning(self, "No Selection", "Please select an order to delay.")
            return
        
        # Get the Order ID and Order Status from the selected row
        order_id_item = self.tblPg1Orders_4.item(current_row, 0)
        status_item = self.tblPg1Orders_4.item(current_row, 1)
        
        if not order_id_item or not status_item:
            QMessageBox.warning(self, "Error", "Could not retrieve order details.")
            return
        
        order_id = order_id_item.text()
        current_status = status_item.text()
        
        # Check if the status is "In Progress"
        if current_status != "in progress":
            QMessageBox.information(self, "Invalid Status", "Only orders with status 'In Progress' can be delayed.")
            return
        
        # Update the order status in the database
        try:
            connection = make_connection(config_file='sqlproject.ini')
            cursor = connection.cursor()
            
            update_query = "UPDATE orders SET order_status = %s WHERE order_id = %s"
            cursor.execute(update_query, ("Order Delayed", order_id))
            connection.commit()
            
            # Update the table widget
            self.tblPg1Orders_4.setItem(current_row, 1, QTableWidgetItem("Order Delayed"))
            
            QMessageBox.information(self, "Success", f"Order ID {order_id} status updated to 'Order Delayed'.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to update order status: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
        self.BtnOrderDelay.clicked.connect(self.delay_order)

    
    
    def delete_customer(self):
        """Delete the selected customer from the database."""
        # Get the currently selected row in the tblCustomers_3 table
        current_row = self.tblCustomers_3.currentRow()
        
        if current_row < 0:
            # No row is selected
            print("Please select a customer to delete.")
            return

        # Get the Customer ID from the selected row (assuming it's in the first column)
        customer_id_item = self.tblCustomers_3.item(current_row, 0)
        
        if not customer_id_item:
            print("Could not retrieve Customer ID.")
            return

        customer_id = customer_id_item.text()

        # Confirm deletion
        confirmation = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete Customer ID {customer_id}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmation == QMessageBox.No:
            return

        try:
            # Establish database connection
            connection = make_connection(config_file='sqlproject.ini')
            cursor = connection.cursor()

            delete_user_portal = "DELETE FROM user_portal JOIN customers ON customer_customer_email = user_portal.user_name WHERE customer_id = %s"
            cursor.execute(delete_user_portal, (customer_id,))
            connection.commit()
            
            # SQL query to delete the customer
            delete_query = "DELETE FROM customers WHERE customer_id = %s"
            cursor.execute(delete_query, (customer_id,))

            # Commit the changes
            connection.commit()

            # Refresh the table
            self.load_customers_data()

            QMessageBox.information(self, "Success", "Customer deleted successfully.")
        except mysql.connector.Error as err:
            QMessageBox.critical(self, "Error", f"Failed to delete customer: {err}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

    # Connect the delete_customer method to the button
        self.BtnDeleteCustomer_3.clicked.connect(self.delete_customer)

    def clear_search(self):
        """Clear customer search inputs and reload data."""
        self.txtCustId_4.clear()
        self.txtSrchCustName_5.clear()
        self.txtSrchCustName_4.clear()
        self.ComboBox_status_order.setCurrentIndex(0)
        self.load_customers_data()

    def clear_payment_search(self):
        """Clear payment search inputs and reload data."""
        self.txtSrchOrderID_11.clear()
        self.comboBox.setCurrentIndex(0)
        self.load_payments_data()

    def setup_navigation(self):
        """Sets up navigation for the QStackedWidget."""
        self.pushButton_1.clicked.connect(lambda: self.EmployeePortalStacked.setCurrentIndex(0))  # Orders
        self.pushButton_2.clicked.connect(lambda: self.EmployeePortalStacked.setCurrentIndex(1))  # Customers
        self.pushButton_3.clicked.connect(lambda: self.EmployeePortalStacked.setCurrentIndex(2))  # Payments
        self.pushButton_4.clicked.connect(self.logout)  # Logout

    def logout(self):
        """Handle logout functionality."""
        open_login_portal(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SellerPortal()
    window.show()
    sys.exit(app.exec_())