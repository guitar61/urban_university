from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# Initialize the FastAPI app
app = FastAPI()

# Initialize the Jinja2Templates object
templates = Jinja2Templates(directory="templates")


# User model
class User(BaseModel):
    id: int
    username: str
    age: int


# List to store user data
users = []


# Route to display all users in the template
@app.get("/", response_class=HTMLResponse)
async def read_users(request: Request):
    # Return the users.html template and pass the request and users list to it
    # Return the users.html template and pass the request and users list to it
    return templates.TemplateResponse("users.html", {"request": request, "users_list": users})


# Route to display a specific user's details
@app.get("/user/{user_id}", response_class=HTMLResponse)
async def read_user(request: Request, user_id: int):
    # Find the user by ID
    user = next((u for u in users if u.id == user_id), None)
    if user is None:
        # Return 404 if the user is not found
        raise HTTPException(status_code=404, detail="User not found")
    # Return the users.html template and pass the request and the found user to it
    return templates.TemplateResponse("users.html", {"request": request, "user": user})


# Route to create a new user
@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int):
    new_id = users[-1].id + 1 if users else 1  # Assign ID based on the last user
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)  # Add the new user to the list
    return new_user


# Route to update user details
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user
    raise HTTPException(status_code=404, detail="User not found")


# Route to delete a user
@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            removed_user = users.pop(index)
            return removed_user
    raise HTTPException(status_code=404, detail="User not found")
