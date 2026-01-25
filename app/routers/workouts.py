from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
    existing = db.query(Workout).filter(
        Workout.name == workout.name
    ).first()

    if existing:
        return existing

    new_workout = Workout(
        name=workout.name,
        category=workout.category,
    )

    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)
    return new_workout

