SkillConnect API

SkillConnect is a backend API built with FastAPI to connect learners with mentors for skill development. The API manages users, skills, and learning sessions, and is ready to be used with a frontend (React, Vue, or any client).

Features

Users – Register learners and mentors with profiles.

Skills – Mentors can add skills and expertise areas.

Sessions – Learners can book sessions with mentors for specific skills.

REST API – Fully functional endpoints for CRUD operations.

SQLite Database – Lightweight, easy to use.

Swagger Docs – Interactive API documentation at /docs.

Project Structure
skillconnect_api/
├─ main.py            # Entry point
├─ database.py        # Database connection
├─ models.py          # SQLAlchemy models
├─ schemas.py         # Pydantic schemas
├─ crud.py            # CRUD helper functions
├─ routers/           # API routers
│   ├─ __init__.py
│   ├─ users.py
│   ├─ skills.py
│   └─ sessions.py
└─ skillconnect.db    # SQLite database

Installation

Clone the repository:

git clone https://github.com/aalliirraazzaa03/Goods_store.git
cd Goods_store


Create and activate a virtual environment:

python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate  # macOS/Linux


Install dependencies:

pip install fastapi uvicorn sqlalchemy pydantic

Running the Server
uvicorn main:app --reload


Server will run at: http://127.0.0.1:8000

Swagger API docs: http://127.0.0.1:8000/docs

ReDoc API docs: http://127.0.0.1:8000/redoc

API Endpoints
Users

POST /users/ – Create a new user

GET /users/ – List all users

Skills

POST /skills/ – Add a new skill

GET /skills/ – List all skills

Sessions

POST /sessions/ – Book a session

GET /sessions/ – List all sessions

Database

Using SQLite (skillconnect.db) for simplicity.

Tables are created automatically on first run.

Contributing

Fork the repository.

Create a feature branch: git checkout -b feature/my-feature

Commit your changes: git commit -m "Add feature"

Push to the branch: git push origin feature/my-feature

Open a Pull Request.

License

This project is licensed under the MIT License.
