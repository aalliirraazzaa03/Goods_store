from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# User Schemas
class UserBase(BaseModel):
    username: str
    email: EmailStr
    is_mentor: bool = False
    bio: Optional[str] = None

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

# Skill Schemas
class SkillBase(BaseModel):
    name: str
    description: Optional[str] = None

class SkillCreate(SkillBase):
    mentor_id: int

class Skill(SkillBase):
    id: int
    mentor_id: int
    class Config:
        orm_mode = True

# Session Schemas
class SessionBase(BaseModel):
    scheduled_at: datetime
    completed: bool = False

class SessionCreate(SessionBase):
    learner_id: int
    skill_id: int

class Session(SessionBase):
    id: int
    learner_id: int
    skill_id: int
    class Config:
        orm_mode = True
