from pydantic import BaseModel


# Schema for creating a new user
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int


# Schema for updating user details
class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int


# Schema for creating a new task
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int


# Schema for updating task details
class UpdateTask(CreateTask):
    pass  # Inherits attributes from CreateTask
