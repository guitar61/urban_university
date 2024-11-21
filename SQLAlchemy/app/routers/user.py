from fastapi import APIRouter

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/")
async def all_users():
    pass  # Placeholder for the function to return all users


@router.get("/{user_id}")
async def user_by_id(user_id: int):
    pass  # Placeholder for the function to return a user by ID


@router.post("/create")
async def create_user():
    pass  # Placeholder for the function to create a new user


@router.put("/update")
async def update_user():
    pass  # Placeholder for the function to update a user


@router.delete("/delete")
async def delete_user():
    pass  # Placeholder for the function to delete a user
