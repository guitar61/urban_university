from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# Create FastAPI instance
app = FastAPI()

# Define the User model using Pydantic
class User(BaseModel):
    id: int
    username: str
    age: int

# Initialize an empty list to store users as a mock database
users = []

# GET request to return the list of users
@app.get("/users")
async def get_users():
    return users

# POST request to add a new user
@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int):
    new_id = users[-1].id + 1 if users else 1  # Assign a new ID based on the last user's ID or 1 if empty
    new_user = User(id=new_id, username=username, age=age)  # Create a new User object
    users.append(new_user)  # Add the new user to the list
    return new_user  # Return the created user

# PUT request to update an existing user's information
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: int, username: str, age: int):
    for user in users:
        if user.id == user_id:  # Check if the user with the given ID exists
            user.username = username  # Update the username
            user.age = age  # Update the age
            return user  # Return the updated user
    raise HTTPException(status_code=404, detail="User was not found")  # Raise an exception if not found

# DELETE request to remove a user
@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:  # Check if the user with the given ID exists
            removed_user = users.pop(index)  # Remove the user from the list
            return removed_user  # Return the removed user
    raise HTTPException(status_code=404, detail="User was not found")  # Raise an exception if not found
