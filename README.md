# 📘 REST API with Flask: User Management
This project implements a REST API using Flask to manage user data with GET, POST, PUT, DELETE methods for practicing API development fundamentals.

## 🚀 Features
✅ Create (POST) a new user
✅ Retrieve (GET) all users or a specific user by ID
✅ Update (PUT) an existing user by ID
✅ Delete (DELETE) a user by ID
✅ Uses in-memory dictionary (no database) for simplicity

## 🛠 Technologies Used
Python

Flask

Postman / Curl (for testing)

REST API concepts (HTTP Methods, JSON, Status Codes)

## 📂 Project Structure

task4_rest_api/
│
├── user_api.py          # Flask app with API routes
├── main.py              # Runs the Flask app
└── README.md            # Project documentation

## ⚙️ How to Run

### 1️⃣ Install dependencies:
--bash

pip install Flask

### 2️⃣ Run the server:

--bash

python main.py

## Your API will be live at:

http://127.0.0.1:5000

## 📌 API Endpoints

### ➡️ Create User
URL: /users

Method: POST

Body (JSON):


{
  "id": "1",
  "name": "Tanmay",
  "email": "tanmay@example.com"
}

Response:


{
  "message": "User added",
  "user": {
    "name": "Tanmay",
    "email": "tanmay@example.com"
  }
}

### ➡️ Get All Users
URL: /users

Method: GET

Response: Returns all users in JSON.

➡️ Get User by ID
URL: /users/<user_id>

Method: GET

Example: /users/1

➡️ Update User
URL: /users/<user_id>

Method: PUT

Body (JSON):

{
  "name": "Tanmay Khairnar",
  "email": "tk@example.com"
}


### ➡️ Delete User
URL: /users/<user_id>

Method: DELETE

## 🧪 Testing with Postman
✅ Open Postman
✅ Enter the endpoint URL (http://127.0.0.1:5000/users)
✅ Select HTTP method (POST, GET, PUT, DELETE)
✅ For POST/PUT, go to Body > raw > JSON, paste your JSON data
✅ Click Send to test your API

## 📖 Interview Concepts Practiced
What is Flask?

What is REST?

HTTP methods: GET, POST, PUT, DELETE

JSON handling with Flask

Request and response objects

Status codes (200, 201, 400, 404)

API testing using Postman

Routing in Flask



## 🙌 Author
Tanmay Khairnar
Your GitHub Profile

