📝 Todo Management Application (FastAPI)

A production-grade Todo Management Web Application built using FastAPI, SQLite, and Jinja2 templates.
The application exposes RESTful APIs for managing tasks and also provides a clean server-rendered web interface.
The project follows SOLID principles, DRY architecture, and avoids using ORM as per assignment requirements.

🚀 Features

RESTful APIs for Todo management (Create & Retrieve)

Server-rendered web UI using Jinja2 templates

SQLite database with raw SQL queries (No ORM)

Clean layered architecture (Router → Controller → Model)

Dependency Injection for database connectors

Separation of concerns (API, Web, DB, Templates, Static files)

Swagger API documentation (Auto-generated)

Production-ready folder structure

Easily extensible to PostgreSQL or other databases

Basic error handling and logging

🛠️ Tech Stack
Layer	Technology
Backend Framework	FastAPI
Database	SQLite
SQL Handling	Raw SQL (No ORM)
Templates	Jinja2
API Docs	OpenAPI / Swagger
Testing	Pytest
Styling	Bootstrap 5
Language	Python 3.10+
📂 Project Structure
todo_app/
│
├── main.py
│
├── routers/
│   ├── api_todos.py
│   └── web_todos.py
│
├── controllers/
│   └── todo_controller.py
│
├── models/
│   └── todo_model.py
│
├── database/
│   └── connectors/
│       ├── base.py
│       └── sqlite.py
│
├── schemas/
│   └── create_todo_schema.py
│
├── templates/
│   ├── base.html
│   └── todos_list.html
│
├── static/
│   └── css/
│       └── style.css
│
├── tests/
│   └── test_todos.py
│
└── README.md

🧠 Architecture Overview

The application follows a layered architecture:

Router Layer
Handles HTTP requests (API & Web)

Controller Layer
Contains request validation, error handling, and orchestration logic

Model Layer
Executes raw SQL queries and interacts with the database

Database Connector Layer
Abstracts database connection logic (SQLite/Postgres ready)

This design ensures loose coupling, testability, and future scalability.

🔗 API Endpoints
Create Todo
POST /todos


Request Body

{
  "title": "Learn FastAPI",
  "description": "Build Todo App",
  "due_date": "2025-01-01",
  "status": "pending"
}


Response

{
  "data": "Todo created successfully"
}

Get All Todos
GET /todos


Response

[
  {
    "title": "Learn FastAPI",
    "description": "Build Todo App",
    "due_date": "2025-01-01",
    "status": "pending"
  }
]

🌐 Web Interface
URL	Description
/	Displays list of todos
/todos/new	Add a new todo

The web interface internally consumes the same business logic as the API, ensuring DRY principles.

⚙️ Setup Instructions
1️⃣ Clone Repository
git clone <your-repo-url>
cd todo_app

2️⃣ Create Virtual Environment
python -m venv todo_venv
source todo_venv/bin/activate   # Linux/Mac
todo_venv\Scripts\activate      # Windows

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Application
uvicorn main:app --reload

📘 API Documentation

Swagger UI available at:

http://127.0.0.1:8000/docs


OpenAPI JSON:

http://127.0.0.1:8000/openapi.json

 