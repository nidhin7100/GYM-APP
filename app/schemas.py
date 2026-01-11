from pydantic import BaseModel
from datetime import datetime

class WorkoutCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True  # Pydantic v2 replaces orm_mode

class Workout(BaseModel):
    id: int
    name: str
    created_at: datetime  # Pydantic automatically converts to ISO string

    class Config:
        from_attributes = True

class SetCreate(BaseModel):
    set_number: int
    weight: int
    reps: int
    rest_seconds: int
