from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.backend.db import Base  # Import Base from db.py

class User(Base):
    __tablename__ = "users"  # Name of the table in the database

    # Columns
    id = Column(Integer, primary_key=True, index=True)  # Primary Key
    username = Column(String, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    slug = Column(String, unique=True, index=True)

    # Relationships
    tasks = relationship("Task", back_populates="user")  # Use string "Task"
