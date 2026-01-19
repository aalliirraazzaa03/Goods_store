from fastapi import FastAPI
import models, database
from routers import users, skills, sessions

from routers.users import router as users_router
from routers.skills import router as skills_router
from routers.sessions import router as sessions_router


app = FastAPI(title="SkillConnect API")

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# Include routers
app.include_router(users.router)
app.include_router(skills.router)
app.include_router(sessions.router)



app.include_router(users_router)
app.include_router(skills_router)
app.include_router(sessions_router)

@app.get("/")
def root():
    return {"message": "Welcome to SkillConnect API"}
