from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import select, insert, update, delete
from app.backend.db_depends import get_db  # Dependency to access DB session
from app.models.user import User  # Import User model
from app.schemas import CreateUser, UpdateUser  # Import Pydantic schemas
from slugify import slugify  # For generating slugs
from typing import Annotated  # Type hint for FastAPI dependencies

# Create a router for user-related routes
router = APIRouter(
    prefix="/user",  # All routes in this file will start with "/user"
    tags=["user"],   # Swagger tag for grouping
)

# Fetch all users
@router.get("/", status_code=200)
def all_users(db: Annotated[Session, Depends(get_db)]):
    """
    Fetch all users from the database.

    :param db: SQLAlchemy session
    :return: List of all users
    """
    stmt = select(User)  # SQLAlchemy SELECT query for all users
    result = db.scalars(stmt).all()  # Execute query and fetch results
    return result


# Fetch a user by ID
@router.get("/{user_id}", status_code=200)
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    """
    Fetch a user by ID.

    :param user_id: ID of the user to fetch
    :param db: SQLAlchemy session
    :return: User object if found
    """
    stmt = select(User).where(User.id == user_id)  # Query to fetch user by ID
    user = db.scalars(stmt).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user


# Create a new user
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user_data: CreateUser, db: Annotated[Session, Depends(get_db)]):
    """
    Create a new user.

    :param user_data: User data from request body
    :param db: SQLAlchemy session
    :return: Success message
    """
    new_user = {
        "username": user_data.username,
        "firstname": user_data.firstname,
        "lastname": user_data.lastname,
        "age": user_data.age,
        "slug": slugify(user_data.username)  # Generate a unique slug
    }
    stmt = insert(User).values(new_user)  # SQLAlchemy INSERT query
    db.execute(stmt)  # Execute the query
    db.commit()  # Commit the transaction
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


# Update a user by ID
@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user_data: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    """
    Update an existing user.

    :param user_id: ID of the user to update
    :param user_data: Updated user data
    :param db: SQLAlchemy session
    :return: Success message
    """
    stmt = select(User).where(User.id == user_id)  # Query to find the user
    user = db.scalars(stmt).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    stmt = (
        update(User)
        .where(User.id == user_id)
        .values(
            firstname=user_data.firstname,
            lastname=user_data.lastname,
            age=user_data.age
        )
    )
    db.execute(stmt)  # Execute the query
    db.commit()  # Commit the transaction
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}


# Delete a user by ID
@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    """
    Delete a user by ID.

    :param user_id: ID of the user to delete
    :param db: SQLAlchemy session
    :return: Success message
    """
    stmt = select(User).where(User.id == user_id)  # Query to find the user
    user = db.scalars(stmt).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    stmt = delete(User).where(User.id == user_id)  # SQLAlchemy DELETE query
    db.execute(stmt)  # Execute the query
    db.commit()  # Commit the transaction
    return {"status_code": status.HTTP_200_OK, "transaction": "User deletion is successful!"}
