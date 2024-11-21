from fastapi import APIRouter

router = APIRouter(prefix="/task", tags=["task"])


@router.get("/")
async def all_tasks():
    pass  # Placeholder for the function to return all tasks


@router.get("/{task_id}")
async def task_by_id(task_id: int):
    pass  # Placeholder for the function to return a task by ID


@router.post("/create")
async def create_task():
    pass  # Placeholder for the function to create a new task


@router.put("/update")
async def update_task():
    pass  # Placeholder for the function to update a task


@router.delete("/delete")
async def delete_task():
    pass  # Placeholder for the function to delete a task




