from fastapi import FastAPI
from app.routers import task, user  # Import the routers for tasks and users

# Create FastAPI application instance
app = FastAPI()

# Root endpoint
@app.get("/")
def welcome_message():
    return {"message": "Welcome to Taskmanager"}

# Include routers from the "routers" folder
app.include_router(user.router)
app.include_router(task.router)

