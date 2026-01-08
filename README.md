FastAPI Blog Application

A full-stack Blog API & Web App built with FastAPI, SQLAlchemy, and PostgreSQL, following clean architecture and best practices.
Supports blog CRUD operations, database migrations, dependency injection, and automated testing.

Features

- FastAPI backend

- RESTful API design

- SQLAlchemy ORM

- PostgreSQL (production) + SQLite (testing)

- Alembic database migrations

- Pydantic schemas (request/response validation)

- Dependency injection

- Jinja2 templates for HTML pages

- Pytest test suite

- Clean project structure (routers, schemas, models, repositories)


Tech Stack

Backend: FastAPI

Database: PostgreSQL

ORM: SQLAlchemy

Migrations: Alembic

Validation: Pydantic v2

Templates: Jinja2

Testing: Pytest

Server: Uvicorn

Project Structure
backend/
├── alembic/
├── apis/
│   ├── base.py
│   └── v1/
│       └── route_blog.py
├── apps/
│   └── base.py
├── core/
│   └── config.py
├── db/
│   ├── base.py
│   ├── models/
│   ├── repository/
│   └── session.py
├── schemas/
│   ├── blog.py
│   └── user.py
├── templates/
│   └── blogs/
│       └── home.html
├── tests/
│   └── test_routes/
├── main.py
└── requirements.txt

Installation & Setup
1. Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd backend

2. Create and activate virtual environment
python -m venv env
source env/bin/activate  # macOS/Linux
env\Scripts\activate     # Windows

4. Install dependencies
pip install -r requirements.txt

5. Environment Variables

Create a .env file:

DATABASE_URL=postgresql://username:password@localhost:5432/blogdb
PROJECT_TITLE=Blog API
PROJECT_VERSION=1.0.0

Database Setup (Alembic)
Create tables
alembic upgrade head

Run the Application
uvicorn main:app --reload --port 5002


API: http://127.0.0.1:5002

Docs (Swagger): http://127.0.0.1:5002/docs

Home Page: http://127.0.0.1:5002/

API Endpoints
Blog
Method	Endpoint	Description
POST	/blog/	Create a blog
GET	/blog/{id}	Get blog by ID
GET	/blog/active_blogs	Get all active blogs
PUT	/blog/{id}	Update a blog
DELETE	/blog/{id}	Delete a blog
Running Tests
pytest


Uses SQLite for isolated test runs

Overrides get_db dependency

Fresh database per test

Learning Outcomes

This project demonstrates:

Clean FastAPI architecture

Proper separation of concerns

Dependency injection

Database session management

API validation with Pydantic

Writing production-ready tests

Future Improvements

Authentication (JWT / OAuth2)

User roles & permissions

Comments & likes

Frontend integration (React / Next.js)

Docker deployment


Author
Manu
Computer Science Student
