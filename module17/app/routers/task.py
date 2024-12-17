from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models import Task, User
from app.schemas import CreateTask, UpdateTask
from ..backend.db import SessionLocal
from slugify import slugify
from sqlalchemy import select


router = APIRouter(prefix="/task", tags=["task"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET all tasks
@router.get("/")
def all_tasks(db: Session = Depends(get_db)):
    tasks = db.scalars(select(Task)).all()
    return tasks

# GET a task by ID
@router.get("/{task_id}")
def task_by_id(task_id: int, db: Session = Depends(get_db)):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# POST to create a new task for a specific user
@router.post("/create")
def create_task(user_id: int, task_data: CreateTask, db: Session = Depends(get_db)):
    user = db.scalars(select(User).where(User.id == user_id)).first()
    if not user:
        raise HTTPException(status_code=404, detail="User was not found")
    new_task = Task(
        title=task_data.title,
        content=task_data.content,
        priority=task_data.priority,
        user_id=user_id,
        slug=slugify(task_data.title)
    )
    db.add(new_task)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}

# PUT to update a task
@router.put("/update/{task_id}")
def update_task(task_id: int, task_data: UpdateTask, db: Session = Depends(get_db)):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = task_data.title
    task.content = task_data.content
    task.priority = task_data.priority
    task.slug = slugify(task_data.title)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task updated successfully"}

# DELETE a task
@router.delete("/delete/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.scalars(select(Task).where(Task.id == task_id)).first()
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    db.delete(task)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "Task deleted successfully"}