import sys
from PyQt5 import uic, QtWidgets

class ReviewWindow(QtWidgets.QMainWindow):
    def __init__(self, product_id, product_name):
        super().__init__()
        uic.loadUi('customer_review_window.ui', self)  # Load the .ui file

        # Set the product name label
        self.label_product_name.setText(f"Product: {product_name}")
        
        # Initialize the submit button click event
        self.pushButton_submit.clicked.connect(self.submit_review)

        # Set up other UI elements as needed
        self.product_id = product_id

    def submit_review(self):
        rating = self.comboBox_rating.currentText()
        review_text = self.plainTextEdit_review.toPlainText()
        
        # Print for demonstration or handle review submission
        print(f"Product ID: {self.product_id}")
        print(f"Rating: {rating}")
        print(f"Review: {review_text}")
        
        # Add code to save or process the review as needed
        QtWidgets.QMessageBox.information(self, "Review Submitted", "Thank you for your review!")

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = ReviewWindow(product_id=1, product_name="Sample Product")
    window.show()
    sys.exit(app.exec_())
