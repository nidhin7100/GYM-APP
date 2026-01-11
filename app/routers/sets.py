from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import SessionLocal
from .. import models, schemas
from typing import List
from pydantic import BaseModel

router = APIRouter()

# Response schema
class WorkoutSetOut(BaseModel):
    id: int
    session_id: int
    set_number: int
    weight: int
    reps: int
    rest_seconds: int

    class Config:
        from_attributes = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{session_id}", response_model=WorkoutSetOut)
def add_set(session_id: int, set_data: schemas.SetCreate, db: Session = Depends(get_db)):
    new_set = models.WorkoutSet(
        session_id=session_id,
        set_number=set_data.set_number,
        weight=set_data.weight,
        reps=set_data.reps,
        rest_seconds=set_data.rest_seconds
    )
    db.add(new_set)
    db.commit()
    db.refresh(new_set)
    return new_set

@router.get("/{session_id}", response_model=List[WorkoutSetOut])
def get_sets(session_id: int, db: Session = Depends(get_db)):
    return db.query(models.WorkoutSet).filter(
        models.WorkoutSet.session_id == session_id
    ).all()
