# 🛒 E-Commerce Management System

> A full-stack, database-driven e-commerce platform with customer, seller, and manager roles, developed using Python, MySQL, and PyQt5.

## 📌 Overview

This project demonstrates the design and implementation of an interactive e-commerce management system integrating operational and analytical modules. Built with **Python**, **MySQL**, and **PyQt5**, it provides tailored portals for customers, sellers, and managers and includes real-time dashboards for performance tracking.

## Introduction

The rapid growth of e-commerce has significantly transformed how businesses manage and organize their data. With millions of customers, transactions, and reviews being generated daily, efficient data management has become essential for the success of online shopping platforms. This project focuses on designing and analyzing a robust e-commerce database using MySQL to address the challenges associated with data management in this dynamic sector.
This project aims to develop a database solution that enhances inventory management, tracks sales trends, and supports strategic decision-making for e-commerce platforms. Creating a functional and intuitive system aims to streamline operations for sellers, managers, and other stakeholders while improving customers' overall shopping experience.
The report will outline the methodology for designing and implementing a comprehensive database system tailored specifically for e-commerce platforms. The integration of user interface elements, such as login pages, customer order histories, and seller portals, demonstrates how functionality and usability are balanced to meet the diverse needs of all users.
This project highlights the importance of robust database design in supporting the operational efficiency and scalability required in modern e-commerce platforms. This ensures that businesses can adapt to the evolving demands of the digital marketplace.

---

## 🧩 Features

### 👤 Customer Portal
- Sign up, log in, and browse products
- Filter and sort items by price and category
- Add to cart, checkout, and track order history
- Write and view product reviews

### 🛍 Seller Portal
- View, manage, and update orders
- Access customer details and delete inactive accounts
- Track payments and order items
- Filter by order ID, status, category, and payment type

### 📊 Manager Portal
- Manage seller information (create, update, delete)
- Visualize:
  - Sales trends over time
  - Customer satisfaction by category
  - Payment method preferences
  - Delivery performance (estimated vs actual)
- Top seller highlights and product category insights

---

## 🧠 Database Design

- **Operational DB**: Includes tables like `orders`, `order_items`, `products`, `customers`, `sellers`, `payments`, `reviews`, and `geolocation`
- **Analytical DB**: Star schema with fact tables (`Fact_Orders`, `Fact_Payments`) and dimension tables (`Dim_Products`, `Dim_Customers`, `Dim_Sellers`, `Dim_Time`)

📌 EER diagrams and schema can be found in `/docs/` folder.

---

## 🔍 Visual Dashboards

> Implemented using PyQt5 charts + SQL queries

- **Monthly Revenue Trends**
- **Customer Satisfaction by Category**
- **Payment Breakdown by Method**
- **Order Status Proportions**
- **Sales by Product Category**

---

## 🧪 Technologies Used

| Component          | Tech Used                          |
|--------------------|------------------------------------|
| Programming        | Python, PyQt5                      |
| Database           | MySQL (Operational & Analytical)   |
| Visualization      | PyQt5 Charts, Matplotlib, Seaborn  |
| Data ETL & Modeling| Pandas, NumPy                      |
| DB Design Tools    | MySQL Workbench, ERDPlus           |
| IDE & UI Design    | VS Code, Qt Designer               |

---

## 🗃 Project Structure

├── sqlmaster.sql # Operational DB schema <br>
├── sqlmaster_wh.sql # Analytical DB schema <br>
├── login_page.py # Login functionality <br>
├── sign_up.py # Sign-up functionality <br>
├── customer_home.py # Customer UI logic <br>
├── seller_portal.py # Seller UI logic <br>
├── manager_portal.py # Manager UI logic <br>
├── shared.py # Shared DB utility functions <br>
├── *.ui # PyQt5 UI files <br>
├── config files # .ini for DB connection


---

## ⚙️ How to Run

1. Download the folder `E-commerce_application_ASQLMaster`.
2. Run the file `login_page.py`.
3. The application includes **three separate portals** for different types of users:
   - **Customer Portal**
   - **Seller Portal**
   - **Manager Portal**

To log in, use the credentials provided below for each portal.  
Alternatively, for the **Customer Portal**, you may create your own account using the **Sign-Up page**.

---

### 🔐 Login Credentials

**Customer Portal**  
- Username: `sandyhsy@gmail.com`  
- Password: `sandy0318`  

**Seller Portal**  
- Username: `lam.n.tran@sjsu.edu`  
- Password: `employee1234`  

**Manager Portal**  
- Username: `khacminhdai.vo@sjsu.edu`  
- Password: `manager1234`


---

## 📚 References

- [Open E-Commerce Dataset by Olist (Kaggle)](https://www.kaggle.com/datasets/terencicp/e-commerce-dataset-by-olist-as-an-sqlite-database)
- [Mockaroo Data Generator](https://www.mockaroo.com/)
- [SimpleMaps ZIP Visualization](https://simplemaps.com/resources/zip-code-visualizations)
- [Adobe Illustrator for Logo Assets](https://www.adobe.com/products/illustrator/logo-design-software.html)

---

## 🧠 Team

Team A SQL Master  
Shao-Yu Huang, Khac Minh Dai Vo, Lam Tran, Aidan Chi  
San Jose State University – Data 201 (Fall 2024)
