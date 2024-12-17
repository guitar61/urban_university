from fastapi import FastAPI
from app.routers import user, task
from app.backend.db import Base, engine

app = FastAPI()

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(user.router)
app.include_router(task.router)

@app.get("/")
def root():
    return {"message": "Welcome to Task Manager!"}
