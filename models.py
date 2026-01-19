from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    is_mentor = Column(Boolean, default=False)
    bio = Column(Text, nullable=True)

    skills = relationship("Skill", back_populates="mentor")
    learner_sessions = relationship("Session", back_populates="learner")

class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(Text, nullable=True)
    mentor_id = Column(Integer, ForeignKey("users.id"))

    mentor = relationship("User", back_populates="skills")
    sessions = relationship("Session", back_populates="skill")

class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True, index=True)
    learner_id = Column(Integer, ForeignKey("users.id"))
    skill_id = Column(Integer, ForeignKey("skills.id"))
    scheduled_at = Column(DateTime, default=datetime.datetime.utcnow)
    completed = Column(Boolean, default=False)

    learner = relationship("User", back_populates="learner_sessions")
    skill = relationship("Skill", back_populates="sessions")
