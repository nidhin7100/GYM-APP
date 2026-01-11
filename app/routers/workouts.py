from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas
from ..schemas import Workout as WorkoutSchema

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    new_w = models.Workout(name=workout.name)
    db.add(new_w)
    db.commit()
    db.refresh(new_w)
    return new_w

@router.get("/", response_model=list[WorkoutSchema])
def create_workout(workout: schemas.WorkoutCreate, db: Session = Depends(get_db)):
    new_w = models.Workout(name=workout.name)
    db.add(new_w)
    db.commit()
    db.refresh(new_w)
    return new_w
