# 💰 Personal Expense Tracker

A simple and user-friendly web application for recording and managing daily expenses. This project was built as a hands-on project to learn how **Python Flask connects the frontend with a backend**.

## ✨ Features

*  Add new expenses
*  Automatically record the expense date
*  Select from predefined categories
*  Add a custom category when needed
*  Automatically calculate total expenses
*  Display all expenses in a table
*  Delete individual expenses
*  Store expense data using a text file
*  Simple and clean user interface

## 🛠️ Technologies Used

 • Python
 • Flask 
 • HTML 
 • CSS 
 • JavaScript

## 📌 About the Project

The application allows users to enter an expense amount and select a category. The date is automatically added when an expense is created.

For common expenses, users can select a category from the dropdown. If the required category is not available, the Other option allows the user to enter a custom category using JavaScript.

Flask handles the form submission and stores the expense information in a text file. The application reads the stored data and displays it on the webpage along with the total amount spent.

The application also allows users to delete individual expenses.

## 📁 Project Structure

```text
expense-tracker-web/
│
├── app.py
├── expenses.txt
├── README.md
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```
## Application webpage 

![Expense Tracker Web App](screenshots/expense%20tracker%20webpage.png)


