from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from backend.db_depends import get_db
from typing import Annotated
from models.user import User  # Adjust import path if needed
from schemas import CreateUser, UpdateUser  # Ensure schemas are defined
from sqlalchemy import insert, select, update, delete
from slugify import slugify


router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=list[CreateUser])
def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users



@router.get("/{user_id}", response_model=CreateUser)
def user_by_id(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")
    return user



@router.post("/create", status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUser, db: Annotated[Session, Depends(get_db)]):
    new_user = User(
        username=user.username,
        firstname=user.firstname,
        lastname=user.lastname,
        age=user.age,
        slug=slugify(user.username)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"status_code": status.HTTP_201_CREATED, "transaction": "Successful"}


@router.put("/update/{user_id}", status_code=status.HTTP_200_OK)
def update_user(user_id: int, user: UpdateUser, db: Annotated[Session, Depends(get_db)]):
    user_to_update = db.scalar(select(User).where(User.id == user_id))
    if user_to_update is None:
        raise HTTPException(status_code=404, detail="User was not found")

    for key, value in user.dict(exclude_unset=True).items():
        setattr(user_to_update, key, value)

    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}


@router.delete("/delete/{user_id}", status_code=status.HTTP_200_OK)
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    user_to_delete = db.scalar(select(User).where(User.id == user_id))
    if user_to_delete is None:
        raise HTTPException(status_code=404, detail="User was not found")

    db.delete(user_to_delete)
    db.commit()
    return {"status_code": status.HTTP_200_OK, "transaction": "User deletion is successful!"}

