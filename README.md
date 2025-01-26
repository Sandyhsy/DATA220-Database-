
San Jose State University
Department of Applied Data Science
Prof Ronald Mak



E-Commerce Management System
Team A SQL Master: Shao-Yu Huang, Khac Minh Dai Vo, Lam Tran, Aidan Chi
December 20th, 2024
Data 201











Table of Contents
Introduction
Application Design
	2.1 Operation Module 
		2.1.1 Customer Operation
2.1.2 Seller Operation
2.1.3 Manager Operation
	2.2 Analytical Module
		2.2.1 Product Sales Over Time
		2.2.2 Payment Value Over Time
Database Design
3.1 Operational Database
3.2 Analytical Database
Working on the Operational Module
Specifications and Usability of Operational Module
5.1 Login Page
5.2 Signup Page
5.3 Customer Portal
5.4 Seller Portal
5.5 Manager Portal
Summary for Operational Module
Summary of Analytical Module
 Technical Aspects
 Database Technical Details
9.1 DB Objects
	9.2 ETL
	9.3 Queries (Analytical DB)
References
Introduction 
The rapid growth of e-commerce has significantly transformed how businesses manage and organize their data. With millions of customers, transactions, and reviews being generated daily, efficient data management has become essential for the success of online shopping platforms. This project focuses on designing and analyzing a robust e-commerce database using MySQL to address the challenges associated with data management in this dynamic sector.
The objective of this project is to develop a database solution that enhances inventory management, tracks sales trends, and supports strategic decision-making for e-commerce platforms. By creating a system that is both functional and intuitive, this project aims to streamline operations for sellers, managers, and other stakeholders, while improving the overall shopping experience for customers.
The report will outline the methodology used to design and implement a comprehensive database system tailored specifically for e-commerce platforms. The integration of user interface elements, such as login pages, customer order histories, and seller portals, demonstrates how functionality and usability are balanced to meet the diverse needs of all users.
This project highlights the importance of robust database design in supporting the operational efficiency and scalability required in modern e-commerce platforms, ensuring that businesses can adapt to the evolving demands of the digital marketplace.

Application Design
2.1 Operation Module:
2.1.1 Customer Operation:
This platform makes it easy for users to browse and shop by allowing them to sort products by price or filter by category. Whether you're looking for books, electronics, or food and beverages, you can quickly narrow down your options. The product table shows the essential details, such as the product ID, category, description, and price. Plus, you can easily add items to your cart with just a plus button click. The feature enhances the shopping experience by helping users easily navigate through a variety of products, enabling them to find items based on their preferences, whether by price or product category.
The cart summary is an e-commerce platform. The user can view the price, quantity, and a delete option for each item in their cart. At the bottom, the total cost of the cart is displayed, which is initially $0.00. There are options to proceed with “Checkout,” “Save,” or “Close” the cart. This interface provides a clean and simple way for users to review their selected items and finalize their purchases.
The order history page, where users can see the status of their past orders. Each order is listed with an order ID, status (e.g., “In progress” or “On the way”), the ordered date, shipped date, and total cost. Below each order, the user can see the details of the purchased items, including product name, unit price, quantity, review score, and a button to “Write a Review” for the product. This feature helps users track their previous purchases and provides the option to leave feedback.

2.1.2 Seller Operation:
Orders Page
The Orders page helps sellers track and manage their orders. It includes key details like order ID, product category, product name, status, price, and quantity. Sellers can filter orders by category, such as books, clothing, or toys, making it easy to find specific products.
A useful feature of this page is the ability to update the order status. Sellers can mark orders as “In Progress”, “On the Way”, or “Order Delayed” to keep customers informed and manage shipping efficiently. The page also displays important dates, like the order date, approval date, and delivery timelines, helping sellers stay organized.
The Order Details section shows a breakdown of products for each order, including product names, categories, prices, and quantities. Buttons like “Ship Order” and “Order Delay” make it simple to update orders quickly. Those functionalities are essential for effective shipping and inventory management.
Customers Page
The Customers page makes it easy to manage customer information. Sellers can search for customers using their ID, first name, last name, or order status. The page displays details like emails, phone numbers, and zip codes, which can be used for customer communication or promotions.
This page also helps sellers identify frequent customers and offer them special deals or promotions to build loyalty. If a customer has an issue, like a shipping delay, sellers can quickly pull up their order history in the Customer Orders Details section, which shows order status, quantity, and delivery dates.
The Delete Customer button allows sellers to remove duplicate accounts or inactive customers, keeping the database clean and organized.
Payments Page
The Payments page provides sellers with a clear overview of payment information. Sellers can search for payments using order ID, customer name, or payment type (like PayPal, Venmo, or credit card). The page shows key details, including installments and payment values, making it easy to track financial transactions.
This data helps sellers identify trends, like which payment methods are most popular or how much customers are spending. The Order Items section gives a detailed view of the products purchased, including categories, quantities, prices, and order dates.
By analyzing this information, sellers can see which products are performing well and which payment methods customers prefer. This page helps sellers make smarter financial decisions and improve their overall business.
2.1.3 Manager Operation:
Seller information preview: Managers can review all the sellers and view all the detailed information such as first name, last name, order sells, and also their address information. 
Modifying seller information: Managers are able to update, delete, search, and create new sellers on this page. Moreover, they can see the products each seller sells.
2.2 Analytical Module
This section is designed for the manager to oversee the e-commerce platform's general performance and should help in informed decisions on how to increase profits or improve the customer's shopping experience.
2.2.1 Product Sales Over Time:
The system provides a “Sales Over Time” dashboard in the Manager Portal, which delivers a detailed visualization of sales trends over specific time periods. Managers can analyze product sales by month, or year to identify growth patterns, seasonal trends, and sales spikes. This capability empowers managers to make informed decisions about promotions, restocking schedules, and long-term sales strategies.

2.2.2 Payment Value Over Time:
Our system also provides a “Payment Value Over Time” dashboard, which gives insights into the trends of the payments and the revenue generated over time. It allows managers to track payment values across various time periods-such as monthly and yearly and further filter those by cash, credit, or online transactions. This helps identify revenue streams, detect abnormal patterns of payments, and assess the effectiveness of payment methods for cash flow optimization and better financial planning.


Database Design


Figure 1: ER Diagram

The figure 1 ER diagram represents a relational database for an e-commerce system, showing all of the detailed entities and the relationships between 9 tables such as orders, order reviews, order items, products, product stocks, sellers, customers, payments, and geolocation. 
The products table, which stores product details such as product ID, description, category, price, dimensions, and weight, has a one-to-many relationship with the product_stock table which enables inventory tracking. Moreover, it also has a many-to-many relationship with the order_items table through a bridge table to log product sales in multiple orders. 
The seller's table contains seller information, including ID, name, email, phone number, and ZIP code, and shares a one-to-many relationship with both the product_stock table for managing inventory and the order_items table for tracking seller-related order details. 
The customers table holds customer details like ID, name, email, and ZIP code, and has a one-to-many relationship with the orders table, where each customer can place multiple orders. 
Additionally, the orders table can track order status, timestamps for purchase, approval date, and delivery dates, and customer IDs, and has a one-to-many relationship with the payments table to manage multiple payments for each order. It also has a one-to-many relationship with the order_reviews table, allowing customers to leave one review per order. 
Lastly, the geolocation table has a one-to-many relationship with sellers and customers via ZIP codes, enabling location-based mapping using attributes like latitude, longitude, city, and state. 
3.1 Operational Database

Figure 2: EER Diagram (Operational Database)

This Enhanced Entity-Relationship (EER) diagram illustrates the structure of an operational database for an e-commerce platform, showing how different entities are interconnected. It includes the user_portal table, which stores user information such as usernames and passwords. The products table holds details about each product, including its ID, description, dimensions, and price. The product_stock table tracks the stock levels for each product and links products to their respective sellers. The sellers table contains information about the platform's sellers, such as their ID, contact details, and location. The orders table represents customer orders, storing order status, timestamps, and delivery dates. Order_items connects orders with products, specifying the quantity and shipping details for each item. The order_payments table manages payment details, including payment type, installments, and amounts. The order_reviews table stores customer feedback for products, including ratings and comments. The customers table contains personal information about customers, while the geolocation table tracks customer addresses, including their city, state, and geographic coordinates. The relationships depicted in the diagram, such as one-to-many between customers and orders, and many-to-many between orders and products, ensure efficient management of e-commerce operations, from product inventory and customer details to order processing and reviews.
3.2 Analytical Database

Figure 3: EER Diagram (Analytical Database)

This Enhanced Entity-Relationship (EER) diagram represents the star schema of a data warehouse for an e-commerce platform, focusing on key aspects such as orders, payments, customers, sellers, and products. The fact tables—Fact_Payments, Fact_Orders, and Fact_Time—are linked to various dimension tables like Dim_Customers, Dim_Sellers, Dim_Products, and Dim_Time. The Dim_Customers table stores detailed customer information such as ID, name, email, phone number, and address. The Dim_Sellers table includes details about sellers, such as their ID, name, contact information, and location. The Dim_Products table describes each product's attributes, including its ID, category, price, and dimensions. The Dim_Time table tracks time-related data, including order dates, year, quarter, month, and day. The Fact_Payments table records payment details like type, value, and installments, while the Fact_Orders table stores order specifics, including product, quantity, and freight value, along with links to customers, sellers, and time. This star schema allows for efficient analysis by simplifying complex queries and enabling fast data retrieval, making it ideal for tracking order performance, payment trends, product sales, and customer behavior on the platform.
Working on the Operational Module
Customers are the primary users of the platform, focused on exploring and purchasing products. They can browse and search for products that interest them, place orders, and review their order history. These functionalities are designed to provide customers with a seamless shopping experience, enabling them to easily find products, make purchases, and track their past transactions for future reference or reviews.
Sellers manage the backend operations related to their products and customers. They have access to browse orders, customer details, payment information, and order items to keep track of their business activities. Sellers can also delete customer accounts when necessary and adjust order statuses like on the way and delayed to ensure accurate updates are provided to customers. Their role is very important in maintaining product availability, order fulfillment, and customer satisfaction.
Managers oversee the overall operations and seller with customer activities on the platform. They can view and adjust seller information and access dashboards to monitor performance metrics and trends. This role focuses on maintaining the integrity of the seller database, ensuring all seller details are up-to-date, and using analytics to support strategic decision-making and improve platform efficiency.

Specifications and Usability of Operational Module
5.1 Log-in Page:
    Figure 4:  Login page with hide password		Figure 5: Login page with unhide password

The Login Page serves as the gateway to the system. Each role (customers, sellers, and managers) has a unique username and password to ensure security, allowing only authorized users to access their accounts. Additionally, the password field includes a toggle option (represented by the monkey covering its eyes image) that allows users to show or hide the entered password. This feature helps users verify their password input in case of uncertainty while maintaining privacy.




5.2 Signup Page:


			


                              



           Figure 7: Password and confirm password









      Figure 6: Inputs for Signup
In figure 6, the Sign-Up Page allows new users to create an account by filling in required details such as their first name, last name, phone number, ZIP code, and email address. Figure 7 shows that the users are also prompted to create a password and confirm it by retyping in the “Retype Password” field. The page includes a password toggle option to view passwords and retype passwords similarly to the Login Page. Once all fields are completed, users can click the “Sign Up” button to register and their account will be added to the database server or use the “Back to Login” button to return to the login page if they already have an account. This simple design ensures an easy and secure registration process.


5.3 Customer Portal:











Figure 8 : Successful login into the customer account
(use username as sandyhsy@gmail.com and password as sandy0318)
The customer can perform four operations: add items to the cart and proceed with checkout, track past orders and check new ones, and provide comments for the orders they have placed.






Figure 9: 
Main order window





5.3.1 Orders
Step 1: Filter and Sort Products by Price



Figure 10:
Filtering and Sorting Products by Category and Price








In Step 1, filter the product category to “Electronics” and sort the items by “Price: High to Low.” The “Sort By” function enables users to arrange the products based on selected criteria, in this case, displaying the most expensive items first.
Step 3: Add Items to Cart 


Figure 11:Add items to Cart



The “Add to Cart” function allows users to add items to their shopping cart by clicking the “+” button next to each product in the list. This feature enables easy selection and purchase of products.
Step 4: Review and Finalize Cart




Figure 12: Review and Finalize Cart











In Step 4, users review the items added to their cart, including product details, prices, and quantities. The total price is displayed at the bottom, and users have the option to delete items, adjust quantities, or proceed to checkout by clicking the “Check Out” button.
Step 5: Adjust Item Quantity in Cart

Figure 13: Adjusting Item Quantity in the Cart


In Step 5, users can modify the quantity of items in their cart by adjusting the number next to each product. For example, the quantity of the “Leather wallet” has been increased from 1 to 2, updating the total price accordingly.
Step 6: Complete the Checkout Process






Figure 14: Order Confirmation After Checkout








In Step 6, after clicking the “Check Out” button, the system processes the order and displays a confirmation message indicating that the order has been placed successfully. The cart is cleared, and the total price is reset to $0.00.








5.3.2 Order History
Step 1: Accessing Order History 





Figure 15: Accessing Order History from User Menu











In this step, click on the user icon located in the top right corner of the screen. A dropdown menu will appear with options such as "Order History" and "Log Out." Click on "Order History" to view your past orders.
Step 2: Search and Order Detail View




Figure 16: Viewing Order Details


This feature allows users to search for specific orders using the “Search orders…” field at the top. After entering a search term, the results are displayed in the first table, which shows key details like order ID, order status (such as “In Progress,” “Shipped,” or “Delivered”), ordered date, shipped date, and total amount. The order status is updated as the seller processes the order. When a user clicks on a specific row in the first table, the second table below dynamically updates to show detailed information about the selected order, including product details, quantity, review score, and review comments. The user can also choose to write a review for the products listed.
5.3.2 Order Review
Step 3: Writing a Product Review








Figure 17:
Writing a Product Review"









In this view, after selecting an order, the product details are displayed in the second table. Each product includes information such as product name, unit price, quantity, review score, and review comments. For each product that has not been reviewed, the user has the option to write a review. By clicking the “Write a Review” button in the “Action” column, the user can provide their feedback, rating, and comments for the order.















Figure 18: Writing and Submitting a Review		       Figure 19: Review Submission Confirmation

In Figure 18, the user is filling out the review form, where they can select a rating (e.g., 5 - Excellent) and write their comments about the product. The “Cancel" and "Submit” buttons are available, allowing the user to either discard or submit the review.
In Figure 19, after clicking “Submit,” a confirmation message appears, thanking the user for their review. If the user attempts to submit the review without providing any comments or a rating, a warning will appear, indicating that the review cannot be submitted until it is properly filled out.
Figure 20: Viewing Updated Review Information After Submission

After submitting the review, the new review information (such as the review score and review comment) is updated in the “Review Score” and “Review Comment” columns for each respective product in the order. In the displayed view, each product now shows a rating of 5 stars and the review comment “I love the order and customer service is so helpful.” These updated details are shown in the second table after the review submission.











5.4 Seller Portal:
 
	Sellers mainly responsible for inventory management and reviewing all of the order details, the customer information and payments for each order of each customer. Seller Portal includes 3 main pages such as Order, Customers and Payments with different interactive buttons.

5.4.1 Order Page:










Figure 21a: Successful login into the seller account
(use username as lam.n.tran@sjsu.edu and password as employee1234)
Figure 21b shows the Order Page in the Seller Portal that provides a comprehensive overview of all orders, enabling sellers to efficiently track and manage them. The page displays the important order details such as Order ID, status, ordered date, order approved date, carrier delivery date, customer delivery date, and estimated delivery date which allows sellers to monitor the progress of each order. Sellers can also filter orders with three different options such as Order ID, Product Category, and Order Status to quickly locate specific records. Below the main table, the Order Details section provides more detailed, product-level information including Product ID, category, name, price, and quantity, for each selected order. The page also features actionable buttons like “Ship Order” and “Order Delay” to update the order status as needed, ensuring smooth order processing and effective customer communication. 
Figure 21b: Main order page

Figure 22: Search order using order id
Figure 22 shows the Search Order by Order ID feature in the Seller Portal that allows sellers to quickly find specific orders by entering the Order ID. It displays all key information specific for that searched order id from both orders and order details tables.
The Search Order by Product Category feature in the Seller Portal allows sellers to filter orders based on specific product categories, such as toys, electronics, or clothing. This makes it easy to focus on orders containing certain types of products. The filtered results display relevant order details, including status, dates, and delivery information, along with the Order Details section showing product-specific information like Product ID, name, price, and quantity. This feature simplifies managing and reviewing category-specific orders efficiently.
Figure 23: Search order using product category

Figure 24 shows the Search Order by Order Status feature which allows sellers to filter orders by their current status like shipped, in progress, delivered, or all. The filtered results provide essential details, including the ordered date, approval date, carrier delivery date, and estimated delivery date, enabling sellers to efficiently track and manage orders at various stages.

Figure 24: Search order using order status
	
Figure 25, 26, 27: Modify the order status to on the way or order delayed.

Figure 25, 26,27 shows the Modify Order Status feature in the Seller Portal which allows sellers to update the status of orders to either “On the Way” or “Order Delayed”. Sellers can only change the status for orders currently marked as "In Progress", as indicated by the yellow warning notification. Once updated, the system provides a confirmation message for the new status with the exclamation mark. This functionality ensures sellers can manage order progress efficiently while keeping customers informed about their order’s current status. The updated order information should be available immediately on the table and the database server. 




5.4.2 Customer Page:
Figure 28 shows the Customer Page in the Seller Portal which allows sellers to view and manage customer information efficiently. Sellers can search for customers using filters like Customer ID, first name, last name, or order status. The displayed results include key details such as email, phone number, and ZIP code, providing all necessary information for customer interactions. Moreover, the Customer Orders Details table at the bottom displays order history, including order ID, status, ordered date, delivery dates, and quantity which allows sellers to track customer purchases and address any issues quickly. This page ensures streamlined customer management and improved service.
Figure 28: Main customer page


	From figure 29 to 32, similarly to the Orders page, Customer page also has an option to search for specific customers using customer id, first name, last name, and order status(delivered, in progress, shipped) which can search all the customer information and their order details. 
Figure 29: Search customer by customer id
Figure 30: Search customer by first name
Figure 31: Search customer by last name


Figure 32: Search customer by order status

Figure 33, 34 illustrates the Delete Customer functionality in the Seller Portal which allows sellers to remove customer records from the database. Upon selecting a customer and clicking the "Delete Customer" button, a confirmation dialog appears, asking for confirmation to proceed. If confirmed, the customer is deleted, and a deleted success message is displayed. This feature helps sellers manage their customer database by removing duplicate or inactive accounts, ensuring the information remains accurate and up-to-date.

Figure 33, 34: Delete customer functionality

5.4.3 Payment Page:
Figure 35 shows the Payment Page in the Seller Portal which provides a detailed overview of payment transactions. Sellers can filter payments by Order ID, customer name, or payment type (e.g., PayPal, credit card, cash). The displayed details include installments, payment values, and customer information such as first name, last name, and customer ID. Additionally, the Order Items section at the bottom provides product-specific details, including category, description, quantity, price, and order date, for each payment. This page helps sellers track financial transactions and analyze customer payment preferences efficiently. This data can also be useful for the business and financial department to find the trend or the preferable payment method. 


Figure 35: Main payment page


	Similarly, figure 36 to 39 shows the payment page that also has options to filter the payment details through order id, customer last name, first name and payment type. And for each payment details, there is also a table below that shows the order items which includes order id, product category or name, product description, quantity of that product, its price, order date to support the transaction area. 

Figure 36: Search payment by order id


Figure 37: Search payment by customer first name



Figure 38: Search payment by customer last name

Figure 39: Search payment by payment type


5.5 Manager Portal:




Figure 40: Successful login into the manager account
(use username as khacminhdai.vo@sjsu.edu and password as manager1234)






5.5.1 Seller Information Page



Figure 41:
Seller Information and Details in Manager Portal

The Manager Portal's Seller Information page allows the user to view a list of sellers with their ID, first and last names, and the number of orders they have processed, displayed in the first table. When a seller's name is clicked, the Sellers Detail table below updates to show more detailed information about that seller, including their email, phone number, zip code, city, and state. This provides an organized and interactive way for the manager to quickly access both summary and detailed information for each seller.
5.5.2 Modify Page





Figure 42:
Modify Seller Information and Products in Manager Portal







The Modify Page in the Manager Portal is designed to help manage seller information and associated products. It consists of three main sections: Search, Seller Information, and Products. In the Search section, the manager can search for a seller by selecting their name from a dropdown menu or by entering their Seller ID, first name, or last name, with a "Search" button to initiate the search. The Seller Information section allows the manager to update existing seller details or create a new seller profile, with editable fields for the seller's First Name, Last Name, State, City, Phone, and Email. Action buttons like “Clear Fields,” “Update Seller,” “Create Seller,” and “Delete Seller” provide options to modify or delete seller information. The Products section displays a table of the seller's associated products, including product ID, category, description, and price, and shows a “No Products!” message if the seller has no products listed. This page streamlines seller management by enabling easy search, modification of seller details, and management of their product listings.
5.5.2.1 Update Seller
Step 1: Selecting Seller


Figure 43:
Step 1 - Selecting Seller in Manager Portal






The “Select Seller” feature allows the manager to choose a seller from a dropdown list of available sellers, which then populates their information in the fields for modification or updating.



Step 2:  Seller Information and Confirmation of Selected Seller ID
Figure 44: Seller Information and ID Confirmation














After clicking the search icon, the seller's information is displayed in the form fields, including their first name, last name, city, phone number, and email. Additionally, a pop-up window appears, confirming the selected seller's ID (in this case, S762), ensuring that the correct seller has been selected. The user can then proceed with updating or managing the seller's details.
Step 3: Edit the Seller's Email Address




Figure 45: 
Editing Seller Email Address








In this step, the manager can modify any information for the selected seller. In this case, the email address is being updated from “eharlick5@clickbank.net” to “danielbrowntexas@clickbank.net.” The manager can make similar changes to other fields, such as the seller’s name, phone number, and city, using the editable fields in the Seller Information section. After making the desired changes, the manager can click “Update Seller” to save the modifications.




Step 4: Click Update Seller







Figure 46: Step 4 - Updating Seller Information          Figure 47: Seller Information Update Confirmation

After clicking the "Update Seller" button, the manager's modifications to the seller's information are saved. A confirmation pop-up window appears, notifying the manager that the seller's information has been successfully updated. This provides clear feedback that the changes have been applied. The updated seller details remain visible on the page, confirming that the update was successful.
5.5.2.1 Create New Seller
Figure 48: Creating a New Seller









Figure 49: New Seller Creation Confirmation         Figure 50: New Seller Added to the Select Seller Dropdown
In this step, the manager fills out the necessary information for a new seller, including the seller's first name, last name, city, state, phone number, and email. After completing the form, the manager clicks the “Create Seller” button. A pop-up window then appears, confirming that the seller (in this case, Seller ID S1002) has been successfully created. The new seller's information is also displayed in the “All Sellers” dropdown list, indicating that the new seller has been added to the system.
5.5.2.2 Delete Seller







Figure 51: Deleting a Seller
















   Figure 52: Seller Deletion Confirmation			Figure 53: Seller Deletion Success


In this step, the manager selects a seller (S1002 Daniel Lee) from the dropdown and decides to delete the seller. After clicking the "Delete Seller" button, a confirmation pop-up window appears, asking if the manager is sure they want to delete the selected seller. Upon confirming by clicking "Yes," another pop-up window appears, notifying the manager that the seller has been deleted successfully.


5.5.3 Sales and Customer Insight
Figure 54: Sales and Customer Insights - No Filters Applied
The Sales and Customer page in the Manager Portal offers various visual insights related to sales performance and customer satisfaction. It includes a Monthly Revenue Trends line chart to track total revenue generated per month, helping the manager identify fluctuations and peak revenue periods. The Customer Satisfaction by Product Categories bar chart displays average customer review scores across different categories such as Home Decor, Books, Food & Beverage, Beauty, Toys, Sports & Outdoors, Clothing, and Electronics, providing valuable insights into customer satisfaction. The Payment Value by Payment Type Over Time bar chart illustrates the total payment value for different payment types (PayPal, Venmo, cash, credit card, and debit card) across months, offering insight into popular payment methods over time. The Order Status Proportions pie chart breaks down the proportions of orders by their current status, including categories like “delivered,” “in process,” and “shipped.” The page also features dropdown menus to filter data by Month, Category, and Status, along with a Refresh button to update the displayed information. This page enables the manager to analyze and track key sales metrics and customer feedback in an easily understandable visual format.
Figure 55: Sales and Customer Insights with February and Beauty Filter

After selecting February as the month and Beauty as the product category, the Sales and Customer Insight page updates to display data specific to these choices. The Monthly Revenue Trends graph now shows the total revenue for February 2018, approximately 310, allowing the manager to track revenue performance for that month. The Customer Satisfaction by Product Categories bar chart reflects an average review score close to 3 for the Beauty category, providing insight into customer satisfaction for Beauty products during the selected period. The Payment Value by Payment Type Over Time chart indicates that credit cards were the predominant payment method in February 2018, with a high payment value for this method. The Order Status Proportions pie chart reveals that 100% of the orders for this selection have been marked as "delivered," giving the manager a clear view of the order fulfillment status. The Refresh button can be clicked to update the visualizations with new filter selections, allowing for tailored and focused data analysis based on the chosen month and product category.
5.5.4 Product and Operations
Figure 56: Product and Operations Analysis
The Product and Operations page in the Manager Portal provides detailed insights into product sales, payment preferences, and delivery performance. It includes a Payment Method Preferences pie chart, which shows the distribution of payment methods used by customers, with credit cards being the most popular. The Product Category Sales by Year and Month bar chart tracks sales by product category over time, with different colors representing categories like Beauty, Books, and Clothing, allowing the manager to analyze monthly sales trends. The Revenue by Product Categories bar chart highlights total revenue generated by various product categories, such as Toys and Clothing, giving a snapshot of the most profitable categories. Additionally, the Delivery Performance (Estimated vs. Actual) bar chart compares estimated delivery times with actual delivery delays, helping assess the efficiency of the delivery process. The top section of the page also displays key metrics, including Total Sales, Total Orders, Average Rating, and the Top Seller, providing an overview of performance indicators. This page allows the manager to effectively monitor and analyze product performance, customer payment preferences, and delivery efficiency.
6. Summary for Operational Module
Customer Operations:
Login and Dashboard: Customers can log in to access a personalized dashboard, which enables them to track both past and current orders, place new orders, and submit reviews.
Orders: Customers can place new orders by adding up to 8 different products to their cart. They can filter products by price, either from low to high or high to low. In the cart, customers have the option to adjust item quantities or remove items. The system automatically generates a unique order_ID for efficient tracking of each order.
Order History: Customers can view the details and status of their past orders. They can also provide feedback and ratings for the products they have received, contributing to the review process for future buyers.
Seller Operations:
Order: allows sellers to view and manage their orders, including order status, delivery dates, and product details. Sellers can filter orders by order ID, product category, or status, and take actions such as shipping orders or marking order delays directly from the portal.
Customers: allows sellers to view and manage customer information, including customer IDs, names, contact details, and order statuses. Sellers can also access customer order details such as order ID, status, delivery dates, and quantities, with options to delete customer records.
Payment: The Payment Details page displays customer payment information, including order IDs, payment types, installments, and payment values, along with a section for Order Items that shows product categories, descriptions, quantities, prices, and order dates, allowing for efficient order and payment tracking.
Manager Operations:
Seller: displays a list of sellers with their Seller ID, First Name, Last Name, and Order Count. Selecting a seller shows detailed information such as their email, phone number, zip code, city, and state.
Modify: allows the manager to manage seller information by selecting a seller from a dropdown or entering their details manually. The page includes options to update, create, or delete sellers, with a section displaying the seller's products, though no products are shown in this instance.
7. Summary of Analytical Module
The Sales and Customer and Product and Operations sections of the Manager Portal offer comprehensive visual insights and key metrics, enabling managers to effectively track business performance, customer satisfaction, and operational efficiency.
Sales and Customer: provides visual insights into key metrics, including monthly revenue trends, customer satisfaction by product categories, payment values by payment type over time, and order status proportions. The page also includes filters for selecting the month, category, and order status, allowing the manager to analyze specific data more effectively.
Product and Operations: provides key insights into sales and operations, including a breakdown of payment method preferences, product category sales by year and month, revenue by product categories, and delivery performance comparing estimated versus actual delivery times. The page also highlights total sales, total orders, average rating, and the top seller for quick performance monitoring.
Both sections in the Manager Portal give managers a clear and detailed picture of the business, allowing them to easily track sales, customer trends, and how efficiently the operations are running. By using these insights, managers can make smarter decisions that enhance customer satisfaction, optimize processes, and drive better sales results.




8. Technical Aspects
No.
File
Type
Comments
1
data201.py
Python
Python database utilities file
2
picture
File
Icon pictures
3
sqlmaster.ini
Config File
Database Config File (Operational)
4
sqlmaster_wh.ini
Config File
Database Config File (Analytical)
5
sqlmaster.sql
SQL Dump
Operational DB Dump
6
sqlmaster_wh.sql
SQL Dump
Analytical DB Dump
7
login_page.py
Python
Login Portal Function
8
login_page.ui
Qt5 UI File 
Login Portal Dialog
9
sign_up.py
Python
Sign Up Portal Function
10
sign_up.ui
Qt5 UI File 
Sign Up Portal Dialog
11
shared.py
Python
Database and Signup/Login Portal utilities
12
customer_home.py
Python
Customer Portal Function
13
customer_home.ui
Qt5 UI File 
Customer Portal Dialog
14
customer_order_history.py
Python
Order History Function
15
customer_order_history.ui
Qt5 UI File 
Order History Dialog
16
customer_review_window.py
Python
Review Window Function
17
customer_review_window.ui
Qt5 UI File 
Review Window Dialog
18
seller_portal.py
Python
Seller Portal Function
19
seller_portal.ui
Qt5 UI File 
Seller Portal Dialog
20
manager_portal.py
Python
Manager Portal Function
21
manager_portal.ui
Qt5 UI File 
Manager Portal Dialog


9.  Database Technical Details
9.1 ETL
9.1.1 Creating tables
DROP TABLE IF EXISTS Fact_Orders;
DROP TABLE IF EXISTS Fact_Payments;
DROP TABLE IF EXISTS Dim_Products;
DROP TABLE IF EXISTS Dim_Customers;
DROP TABLE IF EXISTS Dim_Sellers;
DROP TABLE IF EXISTS Dim_Time;
-- Dim_Time
CREATE TABLE Dim_Time (
    time_id INT AUTO_INCREMENT PRIMARY KEY,
    order_date DATE,
    year INT,
    quarter INT,
    month INT,
    day INT,
    day_of_week VARCHAR(10)
);
-- Dim_Customers
CREATE TABLE Dim_Customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    customer_email VARCHAR(100),
    customer_phone VARCHAR(50),
    customer_zip_code INT,
    city VARCHAR(100),
    state VARCHAR(100),
    country VARCHAR(100) DEFAULT 'USA'
);
-- Dim_Sellers
CREATE TABLE Dim_Sellers (
    seller_id VARCHAR(200) PRIMARY KEY,
    seller_name VARCHAR(255),
    seller_email VARCHAR(100),
    seller_phone VARCHAR(50),
    seller_zip_code INT,
    city VARCHAR(100),
    state VARCHAR(100)
);
-- Dim_Products
CREATE TABLE Dim_Products (
    product_id VARCHAR(200) PRIMARY KEY,
    product_category VARCHAR(100),
    product_price DECIMAL(10, 2),
    product_length DOUBLE,
    product_width DOUBLE,
    product_height DOUBLE,
    product_weight DOUBLE
);




-- Fact_Orders
CREATE TABLE Fact_Orders (
    fact_order_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id VARCHAR(200),
    customer_id INT,
    seller_id VARCHAR(200),
    time_id INT,
    freight_value DOUBLE,
    quantity INT,
    FOREIGN KEY (product_id) REFERENCES Dim_Products(product_id),
    FOREIGN KEY (customer_id) REFERENCES Dim_Customers(customer_id),
    FOREIGN KEY (seller_id) REFERENCES Dim_Sellers(seller_id),
    FOREIGN KEY (time_id) REFERENCES Dim_Time(time_id)
);
-- Fact_Payments
CREATE TABLE Fact_Payments (
    fact_payment_id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    product_id VARCHAR(200), 
    customer_id INT,
    seller_id VARCHAR(200), 
    time_id INT,
    payment_type VARCHAR(100),
    payment_installments DOUBLE,
    payment_value DOUBLE,
    FOREIGN KEY (product_id) REFERENCES Dim_Products(product_id),
    FOREIGN KEY (customer_id) REFERENCES Dim_Customers(customer_id),
    FOREIGN KEY (seller_id) REFERENCES Dim_Sellers(seller_id),
    FOREIGN KEY (time_id) REFERENCES Dim_Time(time_id)
);

9.1.2 ETL

Usage
Code
Importing packages
import pandas as pd
from datetime import datetime
import mysql.connector
Connecting to different schemas
src_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sandy0318",
    database="asqlmaster_project"
)

tgt_conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sandy0318",
    database="assign9"
)
Extract data function
def extract(query, connection):
    """Extract data from source database."""
    return pd.read_sql(query, connection)
Load DataFrame into the target table


def load_data(df, table_name, connection):
    """Load DataFrame into the target table."""
    cursor = connection.cursor()
    for _, row in df.iterrows():
        placeholders = ", ".join(["%s"] * len(row))
        columns = ", ".join(row.index)
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        try:
            cursor.execute(query, tuple(row))
        except mysql.connector.Error as e:
            print(f"Error inserting row into {table_name}: {e}")
    connection.commit()
    cursor.close()
Retrieve Product Details
products_query = """
    SELECT product_id, product_category, product_price, 
           product_length, product_width, product_height, product_weight
    FROM products;
"""
Retrieve Customer Details and Location
customers_query = """
    SELECT c.customer_id, CONCAT(c.customer_first_name, ' ', c.customer_last_name) AS customer_name, 
           c.customer_email, c.customer_phone, g.city, g.state_name AS state, c.customer_zip_code
    FROM customers c
    JOIN geolocation g ON c.customer_zip_code = g.zip;
"""
Retrieve Seller Details and Location
sellers_query = """
    SELECT s.seller_id, CONCAT(s.seller_first_name, ' ', s.seller_last_name) AS seller_name, 
           s.seller_email, s.seller_phone, g.city, g.state_name AS state, s.seller_zip_code
    FROM sellers s
    JOIN geolocation g ON s.seller_zip_code = g.zip;
"""
Retrieve Order and Product Details
orders_query = """
    SELECT o.order_id, o.customer_id, ot.seller_id, ot.product_id, ot.freight_value, ot.quantity, o.order_purchase_timestamp
    FROM orders o
    JOIN order_items ot ON o.order_id = ot.order_id;
"""
Retrieve Payment and Order Details
payments_query = """
    SELECT o.order_id, o.customer_id, s.seller_id, oi.product_id, op.payment_type, op.payment_installments, op.payment_value, o.order_purchase_timestamp
    FROM orders o
    JOIN order_payments op ON o.order_id = op.order_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN sellers s ON s.seller_id = oi.seller_id;
"""
Extract Data
products_df = extract(products_query, src_conn)
customers_df = extract(customers_query, src_conn)
sellers_df = extract(sellers_query, src_conn)
orders_df = extract(orders_query, src_conn)
payments_df = extract(payments_query, src_conn)
Time Dimension Transformation
# Transformations for Dim_Time
time_data = pd.DataFrame({
    "order_date": pd.to_datetime(orders_df["order_purchase_timestamp"]),
})
time_data["year"] = time_data["order_date"].dt.year
time_data["quarter"] = time_data["order_date"].dt.quarter
time_data["month"] = time_data["order_date"].dt.month
time_data["day"] = time_data["order_date"].dt.day
time_data["day_of_week"] = time_data["order_date"].dt.day_name()
time_data["time_id"] = time_data.index + 1
Merge time_id with orders and payments
orders_df = orders_df.merge(time_data[["time_id", "order_date"]], 
                            left_on="order_purchase_timestamp", 
                            right_on="order_date", 
                            how="left").drop(columns=["order_date"])
payments_df = payments_df.merge(time_data[["time_id", "order_date"]], 
                                left_on="order_purchase_timestamp", 
                                right_on="order_date", 
                                how="left").drop(columns=["order_date"])
Load Data
load_data(products_df, "Dim_Products", tgt_conn)
load_data(customers_df, "Dim_Customers", tgt_conn)
load_data(sellers_df, "Dim_Sellers", tgt_conn)
load_data(time_data[["time_id", "order_date", "year", "quarter", "month", "day", "day_of_week"]], "Dim_Time", tgt_conn)
load_data(orders_df[["order_id", "product_id", "customer_id", "seller_id", "time_id", "freight_value", "quantity"]], "Fact_Orders", tgt_conn)
load_data(payments_df[["order_id", "product_id", "customer_id", "seller_id", "time_id", "payment_type", "payment_installments", "payment_value"]], "Fact_Payments", tgt_conn)

src_conn.close()
tgt_conn.close()





9.1.3 Queries (Operation DB)

Usage
Query
Populate sellers table in Manager Portal
SELECT s.seller_id, s.seller_first_name, s.seller_last_name, COUNT(i.seller_id) AS order_count
FROM sellers s
LEFT JOIN order_items i ON s.seller_id = i.seller_id
GROUP BY s.seller_id, s.seller_first_name, s.seller_last_name
ORDER BY order_count DESC;
Display Seller Details in Manager Portal
SELECT s.seller_id, s.seller_email, s.seller_phone, s.seller_zip_code, g.city, g.state_name
FROM sellers s 
JOIN geolocation g ON g.geolocation_id = s.seller_zip_code
WHERE s.seller_id = %s;
Populate Sellers Dropdown in Manager Portal
SELECT DISTINCT seller_id, CONCAT(seller_first_name, ' ', seller_last_name) AS full_name
FROM sellers
ORDER BY full_name;
Populate States in Manager Portal
SELECT DISTINCT state_name 
FROM geolocation 
ORDER BY state_name;
Populate Cities in Manager Portal
SELECT DISTINCT city 
FROM geolocation 
ORDER BY city;
Update Cities based on State in Manager Portal
SELECT DISTINCT city 
FROM geolocation 
WHERE state_name = %s 
ORDER BY city;
Search for Sellers in Manager Portal
SELECT seller_id, seller_first_name, seller_last_name, seller_email, seller_phone
FROM sellers
WHERE (%s IS NULL OR seller_id = %s)
AND (%s IS NULL OR seller_first_name LIKE %s)
AND (%s IS NULL OR seller_last_name LIKE %s);
Update Seller from Dropdown in Manager Portal
SELECT seller_id, seller_first_name, seller_last_name, seller_email, seller_phone
FROM sellers
WHERE seller_id = %s
Display Seller Information in Manager Portal
SELECT DISTINCT city, state_name
FROM geolocation
WHERE geolocation_id = (
SELECT seller_zip_code FROM sellers WHERE seller_id = %s);
Display the seller  product in Manager Portal
SELECT p.product_id, p.product_category, p.product_description, p.product_price
FROM products p
JOIN product_stock ps ON ps.product_id = p.product_id
JOIN sellers s ON ps.seller_id = s.seller_id
WHERE s.seller_id = %s;
Fetch ZIP code based on city and state in Manager Portal
SELECT geolocation_id
FROM geolocation
WHERE city = %s AND state_name = %s;
Update seller information in Manager Portal
UPDATE sellers
SET seller_first_name = %s, seller_last_name = %s, seller_email = %s, seller_phone = %s, seller_zip_code = %s
WHERE seller_id = %s;
Delete Seller in Manager Portal (With deleting all the constraints)
SELECT COUNT(*) FROM products p JOIN product_stock ps ON ps.product_id = p.product_id WHERE seller_id = %s", (seller_id,);

DELETE FROM products p JOIN product_stock ps ON ps.product_id = p.product_id WHERE seller_id = %s", (seller_id,);

SELECT COUNT(*) FROM product_stock WHERE seller_id = %s", (seller_id,);

DELETE FROM product_stock WHERE seller_id = %s", (seller_id,);
            
DELETE FROM sellers WHERE seller_id = %s", (seller_id,);
Create new Seller in Manager Portal
SELECT geolocation_id FROM geolocation WHERE city = %s AND state_name = %s LIMIT 1;

INSERT INTO sellers (seller_id, seller_first_name, seller_last_name, 
                                    seller_email, seller_phone, seller_zip_code)
VALUES (%s, %s, %s, %s, %s, %s);
Creating new seller id in Manager Portal
SELECT seller_id FROM sellers WHERE seller_id REGEXP '^S[0-9]+';
Populate order status in Manager Portal
SELECT DISTINCT order_status
FROM orders
ORDER BY order_status;
Display chart Revenue trend in Manager Portal
SELECT DATE_FORMAT(order_purchase_timestamp, '%Y-%m') AS year_and_month, 
                        SUM(payment_value) AS total_revenue
                    FROM orders
                    JOIN order_payments ON orders.order_id = order_payments.order_id
                    GROUP BY DATE_FORMAT(order_purchase_timestamp, '%Y-%m')
                    ORDER BY year_and_month;
Customer Satisfaction in Manager Portal
SELECT products.product_category, AVG(order_reviews.review_score) AS avg_review_score
                    FROM products
                    JOIN order_items ON products.product_id = order_items.product_id
                    JOIN orders ON order_items.order_id = orders.order_id
                    JOIN order_reviews ON orders.order_id = order_reviews.order_id
                    GROUP BY products.product_category;
Payment Value Over Time in Manager Portal
SELECT products.product_id as product_id, orders.order_id as order_id, Month(orders.order_purchase_timestamp) as month
FROM products
JOIN order_items ON products.product_id = order_items.product_id
JOIN orders ON orders.order_id = order_items.order_id
WHERE {conditions};
Order Status proportion in Manager Portal


SELECT orders.order_status, COUNT(*) AS status_count
FROM orders
JOIN order_items ON order_items.order_id = orders.order_id
JOIN products ON products.product_id = order_items.product_id
WHERE {conditions}
GROUP BY orders.order_status;
Total sales in Manager Portal


SELECT SUM(payment_value) AS total_sales 
FROM order_payments
Total orders in Manager Portal
SELECT COUNT(*) AS total_orders FROM orders;
Avg rating in Manager Portal


SELECT AVG(review_score) AS avg_rating FROM order_reviews;
Top seller in Manager Portal


SELECT CONCAT(s.seller_id, ' - ', s.seller_last_name, ' ', s.seller_first_name) AS top_seller
FROM sellers s
JOIN order_items oi ON oi.seller_id = s.seller_id
JOIN orders o ON o.order_id = oi.order_id
JOIN order_payments op ON op.order_id = o.order_id
GROUP BY s.seller_id
ORDER BY SUM(op.payment_value) DESC 
LIMIT 1;
Payment Method preferences in Manager Portal
SELECT payment_type, COUNT(*) AS count
FROM order_payments
GROUP BY payment_type;
Revenue by product categories in Manager Portal
SELECT p.product_category, SUM(op.payment_value) AS total_revenue
FROM products p
JOIN order_items oi ON p.product_id = oi.product_id
JOIN orders o ON oi.order_id = o.order_id
JOIN order_payments op ON o.order_id = op.order_id
GROUP BY p.product_category;
Delivery_Performance in Manager Portal
SELECT DATEDIFF(order_delivered_customer_date, order_estimated_delivery_date) AS delivery_delay, COUNT(*) AS count
FROM orders
WHERE order_delivered_customer_date IS NOT NULL
GROUP BY delivery_delay;


9.1.4 Queries (Analytical DB)

Usage
Query
Populate month for dropdowns in Manager Portal
SELECT DISTINCT month
FROM Dim_Time
ORDER BY month;
Populate product category in Manager Portal
SELECT DISTINCT product_category
FROM Dim_Products
ORDER BY product_category;
Payment Value Over Time in Manager Portal
SELECT d_t.year, d_t.month, f.payment_type, SUM(f.payment_value) AS total_payment_value
FROM Fact_Payments f
JOIN Dim_Time d_t ON f.time_id = d_t.time_id
GROUP BY d_t.year, d_t.month, f.payment_type
ORDER BY d_t.year, d_t.month, total_payment_value DESC;
Product Sales Over Time in Manager Portal
SELECT d_t.year, d_t.month,  d_p.product_category, SUM(f.quantity) AS total_quantity, SUM(f.freight_value) AS total_freight_value
FROM Fact_Orders f
JOIN Dim_Products d_p ON f.product_id = d_p.product_id
JOIN Dim_Time d_t ON f.time_id = d_t.time_id
GROUP BY d_t.year, d_t.month, d_p.product_category
ORDER BY d_t.year, d_t.month, d_p.product_category;

10. References
10.1. Works Cited
[1] Terencicp. “E-Commerce Dataset by Olist as an SQLite Database.” Kaggle, [2024], https://www.kaggle.com/datasets/terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database?select=olist.sqlite
[2] Mockaroo. Mockaroo - Random Data Generator. Mockaroo, 2023, https://www.mockaroo.com/
[3] SimpleMaps. ZIP Code Visualizations. SimpleMaps, 2023, https://simplemaps.com/resources/zip-code-visualizations.
[4] Adobe https://www.adobe.com/products/illustrator/logo-design-software.html
10.2. Application Design
The tools and libraries used during the development process include the following:
Development Tools:
Python (Primary programming language)
MySQL Workbench (Database management)
PyQt Designer (GUI development)
ERD Plus (ER diagram design)
Visual Studio Code (Code editor and IDE)

Additional Python Packages:
Pandas – For data manipulation and analysis
NumPy – For numerical computations
Matplotlib – For data visualization
Seaborn – For advanced statistical visualizations
PyQt5 and PyQt5-Tools – For building graphical user interfaces
MySQL Connector for Python – To connect Python with MySQL databases
