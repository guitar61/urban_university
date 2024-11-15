from fastapi import FastAPI

# Create FastAPI instance
app = FastAPI()

# Initial users dictionary as a mock database
users = {'1': 'Name: Example, Age: 18'}


# GET route for retrieving all users
@app.get("/users")
async def get_users():
    return users


# POST route to add a new user
@app.post("/user/{username}/{age}")
async def add_user(username: str, age: int):
    new_id = str(max(int(i) for i in users.keys()) + 1)
    users[new_id] = f"Name: {username}, Age: {age}"
    return f"User {new_id} is registered"


# PUT route to update user information
@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    users[user_id] = f"Name: {username}, Age: {age}"
    return f"The user {user_id} has been updated"


# DELETE route to remove a user
@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    users.pop(user_id, None)
    return f"User {user_id} has been deleted"
