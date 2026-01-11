from fastapi import APIRouter, Depends
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

# Create a workout
@router.post("/", response_model=schemas.WorkoutRead)
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    new_w = models.Workout(name=workout.name)
    db.add(new_w)
    db.commit()
    db.refresh(new_w)
    return new_w

# Get all workouts
@router.get("/", response_model=list[schemas.WorkoutRead])
def get_workouts(db: Session = Depends(get_db)):
    return db.query(models.Workout).all()
