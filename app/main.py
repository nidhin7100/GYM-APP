from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .database import Base, engine
from .routers import workouts, sessions, sets

Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]  # Allow all origins for testing

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(workouts.router, prefix="/workouts")
app.include_router(sessions.router, prefix="/sessions")
app.include_router(sets.router, prefix="/sets")
