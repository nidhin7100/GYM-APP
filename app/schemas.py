from pydantic import BaseModel

class WorkoutCreate(BaseModel):
    name: str

class SetCreate(BaseModel):
    set_number: int
    weight: int
    reps: int
    rest_seconds: int
