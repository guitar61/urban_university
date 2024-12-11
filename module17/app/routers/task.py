from fastapi import APIRouter

router = APIRouter(
    prefix="/task",
    tags=["task"]
)

@router.get("/")
def all_tasks():
    """Return all tasks"""
    return {"message": "All tasks"}

@router.get("/{task_id}")
def task_by_id(task_id: int):
    """Return a task by ID"""
    return {"message": f"Task with ID {task_id}"}

@router.post("/create")
def create_task():
    """Create a new task"""
    return {"message": "Task created successfully"}

@router.put("/update/{task_id}")
def update_task(task_id: int):
    """Update an existing task"""
    return {"message": f"Task with ID {task_id} updated"}

@router.delete("/delete/{task_id}")
def delete_task(task_id: int):
    """Delete a task"""
    return {"message": f"Task with ID {task_id} deleted"}
