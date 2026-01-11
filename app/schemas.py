from pydantic import BaseModel

# For creating a new workout
class WorkoutCreate(BaseModel):
    name: str

    model_config = {
        "from_attributes": True  # replaces orm_mode in Pydantic v2
    }

# For returning workouts to the client
class WorkoutRead(BaseModel):
    id: int
    name: str
    created_at: str  # or datetime if you want

    model_config = {
        "from_attributes": True
    }

# For adding a set
class SetCreate(BaseModel):
    set_number: int
    weight: int
    reps: int
    rest_seconds: int
