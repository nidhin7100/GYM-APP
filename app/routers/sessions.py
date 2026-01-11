from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas
from typing import List
from datetime import datetime
from pydantic import BaseModel

router = APIRouter()

# Response schema
class WorkoutSessionOut(BaseModel):
    id: int
    workout_id: int
    date: datetime

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{workout_id}", response_model=WorkoutSessionOut)
def start_session(workout_id: int, db: Session = Depends(get_db)):
    new_session = models.WorkoutSession(workout_id=workout_id)
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

@router.get("/{workout_id}", response_model=List[WorkoutSessionOut])
def get_sessions(workout_id: int, db: Session = Depends(get_db)):
    return db.query(models.WorkoutSession).filter(
        models.WorkoutSession.workout_id == workout_id
    ).all()
