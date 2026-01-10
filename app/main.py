from fastapi import FastAPI
from .database import Base, engine
from .routers import workouts, sessions, sets

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(workouts.router, prefix="/workouts")
app.include_router(sessions.router, prefix="/sessions")
app.include_router(sets.router, prefix="/sets")
