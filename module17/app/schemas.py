from pydantic import BaseModel

# User Schemas
class CreateUser(BaseModel):
    username: str
    firstname: str
    lastname: str
    age: int

class UpdateUser(BaseModel):
    firstname: str
    lastname: str
    age: int

# Task Schemas
class CreateTask(BaseModel):
    title: str
    content: str
    priority: int = 0

class UpdateTask(BaseModel):
    title: str
    content: str
    priority: int
