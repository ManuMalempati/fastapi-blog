FastAPI Blog Application

A full-stack Blog API and Web App built with FastAPI, SQLAlchemy, and PostgreSQL. Supports full blog CRUD operations, authentication, HTML templates, and clean backend architecture.

Live Demo: https://fastapi-blog-pwej.onrender.com

Features

FastAPI backend with RESTful API design

SQLAlchemy ORM

PostgreSQL in production and SQLite for testing

Alembic database migrations

Pydantic v2 schemas

Jinja2 templates for server-rendered pages

JWT authentication using secure cookies

Clean project structure with routers, models, schemas, and repositories

Pytest test suite

Tech Stack
Backend: FastAPI
Database: PostgreSQL
ORM: SQLAlchemy
Migrations: Alembic
Validation: Pydantic v2
Templates: Jinja2
Testing: Pytest
Server: Uvicorn

Installation and Setup

Clone the repository
git clone https://github.com/your-username/your-repo-name.git
cd backend

Create and activate a virtual environment
python -m venv env
source env/bin/activate   (macOS/Linux)
env\Scripts\activate      (Windows)

Install dependencies
pip install -r requirements.txt

Create a .env file
DATABASE_URL=postgresql://username:password@localhost:5432/blogdb
PROJECT_TITLE=Blog API
PROJECT_VERSION=1.0.0
SECRET_KEY=your-secret-key
ALGORITHM=HS256

Run database migrations
alembic upgrade head

Start the application
uvicorn main:app --reload --port 5002

Local URLs
API Root: http://127.0.0.1:5002
Swagger Docs: http://127.0.0.1:5002/docs
Home Page: http://127.0.0.1:5002/
Production Deployment: https://fastapi-blog-pwej.onrender.com

API Endpoints

Blog:
POST /blog/ - Create a blog
GET /blog/{id} - Get blog by ID
GET /blog/active_blogs - Get all active blogs
PUT /blog/{id} - Update a blog
DELETE /blog/{id} - Delete a blog

Running Tests
pytest

Uses SQLite for isolated test runs with dependency overrides.

Learning Outcomes
Clean FastAPI architecture
Dependency injection
Database session management
Pydantic validation
Alembic migrations
Writing maintainable backend code
Building a full-stack FastAPI app with templates

Author
Manu
Computer Science Student
