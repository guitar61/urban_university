from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from slugify import slugify
from typing import Annotated
from app.backend.db_depends import get_db
from app.models.user import User
from app.schemas import CreateUser, UpdateUser

router = APIRouter(
    prefix="/user",
    tags=["user"]
)

# Dependency to get the database session
DBSession = Annotated[Session, Depends(get_db)]

# Route to fetch all users
@router.get("/", status_code=status.HTTP_200_OK)
def all_users(db: DBSession):
    stmt = select(User)
    users = db.scalars(stmt).all()
    return users

# Route to fetch a user by ID
@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def user_by_id(user_id: int, db: DBSession):
    stmt = select(User).where(User.id == user_id)
    user = db.scalar(stmt)  # Corrected logic: using .scalar() instead of .scalars()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user

# Route to create a new user
@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: DBSession):
    slug = slugify(user.username)
    stmt = insert(User).values(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slug
    )
    db.execute(stmt)
    db.commit()
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}

# Route to update a user
@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, updated_user: UpdateUser, db: DBSession):
    stmt = select(User).where(User.id == user_id)
    user = db.scalar(stmt)  # Corrected logic: using .scalar()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    # Update the user
    stmt = (
        update(User)
        .where(User.id == user_id)
        .values(
            firstname=updated_user.firstname,
            lastname=updated_user.lastname,
            age=updated_user.age
        )
    )
    db.execute(stmt)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}

# Route to delete a user
@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: DBSession):
    stmt = select(User).where(User.id == user_id)
    user = db.scalar(stmt)  # Corrected logic: using .scalar()
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    # Delete the user
    stmt = delete(User).where(User.id == user_id)
    db.execute(stmt)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User deleted successfully"}
