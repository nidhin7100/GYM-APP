from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.Workout)
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    new_w = models.Workout(name=workout.name, category=workout.category)
    db.add(new_w)
    db.commit()
    db.refresh(new_w)
    return new_w

@router.get("/", response_model=List[schemas.Workout])
def get_workouts(db: Session = Depends(get_db)):
    return db.query(models.Workout).all()
