from fastapi import FastAPI

# making an instance of the FastApi class
app = FastAPI()


@app.get("/")
async def read_main():
    return {"message": "Main Page"}


@app.get("/user/admin")
async def read_admin():
    return {"message": "You are logged in as an administrator"}


@app.get("/user/{user_id}")
async def read_user(user_id: int):
    return {"message": f"You are logged in as user #{user_id}"}


@app.get("/user")
async def user_info(username: str, age: int):
    return {"message": f"User information. Name: {username}, Age: {age}"}


