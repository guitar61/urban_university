from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()


@app.get("/user/{user_id}")
async def read_user(
        user_id: Annotated[int, Path(title="Enter User ID", ge=1, le=100, example=1)]
):
    return{"message":f"you have entered user ID {user_id}"}


@app.get("/user/{username}/{age}")
async def user_info(
        username: Annotated[str, Path(title="Enter username", min_length=5, max_length=20, example='UrbanUser')],
        age: Annotated[int, Path(title="Enter Your Age", ge=18, le=120, example=24)]
):
    return{message: f"Username: {username}, Age: {age}"}