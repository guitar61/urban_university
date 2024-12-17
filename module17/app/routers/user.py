from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import User, Task
from app.schemas import CreateUser, UpdateUser
from ..backend.db import SessionLocal
from sqlalchemy import select, delete



router = APIRouter(prefix="/user", tags=["user"])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# POST to create a new user
@router.post("/create")
def create_user(user: CreateUser, db: Session = Depends(get_db)):
    # Check if username already exists
    existing_user = db.scalars(select(User).where(User.username == user.username)).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    # Create a new user
    new_user = User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful", "user": new_user}


# GET all tasks for a specific user
@router.get("/{user_id}/tasks")
def tasks_by_user_id(user_id: int, db: Session = Depends(get_db)):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user.tasks

# DELETE a user and all their associated tasks
@router.delete("/delete/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # Delete associated tasks first
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.delete(user)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User and associated tasks deleted successfully"}