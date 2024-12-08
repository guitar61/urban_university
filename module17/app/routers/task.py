from fastapi import APIRouter

# Create a router for task-related routes
router = APIRouter(
    prefix="/task",  # All routes in this file will start with "/task"
    tags=["task"],   # Swagger tag for grouping
)

@router.get("/")
def all_tasks():
    return {"message": "List of all tasks"}

@router.get("/task_id")
def task_by_id(task_id: int):
    return {"message": f"Details of task {task_id}"}

@router.post("/create")
def create_task():
    return {"message": "Task created"}

@router.put("/update")
def update_task():
    return {"message": "Task updated"}

@router.delete("/delete")
def delete_task():
    return {"message": "Task deleted"}
