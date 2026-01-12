from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class Workout(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    category = Column(String, nullable=False) 
    created_at = Column(DateTime, default=datetime.utcnow)

    sessions = relationship("WorkoutSession", back_populates="workout")

class WorkoutSession(Base):
    __tablename__ = "sessions"

    id = Column(Integer, primary_key=True, index=True)
    workout_id = Column(Integer, ForeignKey("workouts.id"))
    date = Column(DateTime, default=datetime.utcnow)

    workout = relationship("Workout", back_populates="sessions")
    sets = relationship("WorkoutSet", back_populates="session")

class WorkoutSet(Base):
    __tablename__ = "sets"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("sessions.id"))
    set_number = Column(Integer)
    weight = Column(Integer)
    reps = Column(Integer)
    rest_seconds = Column(Integer)

    session = relationship("WorkoutSession", back_populates="sets")

