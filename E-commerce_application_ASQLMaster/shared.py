# shared.py
import mysql.connector
from PyQt5 import QtWidgets
from data201 import make_connection

def connect_to_database():
    """
    Establish a connection to the MySQL database.
    """
    try:
        return make_connection(config_file = 'sqlproject.ini')

    except mysql.connector.Error as e:
        QtWidgets.QMessageBox.critical(None, "Database Error", f"Error connecting to the database: {e}")
        return None

def open_login_portal(current_window):
    """
    Close the current window and open the login portal.
    """
    from login_page import LoginPage  # Import here to avoid circular imports
    login_portal = LoginPage()
    login_portal.show()
    current_window.close()

def open_signup_portal(current_window):
    """
    Close the current window and open the signup portal.
    """
    from sign_up import SignUpPage  # Import here to avoid circular imports
    signup_portal = SignUpPage()
    signup_portal.show()
    current_window.close()