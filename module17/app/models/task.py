from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.backend.db import Base  # Import Base from db.py

class Task(Base):
    __tablename__ = "tasks"  # Name of the table in the database

    # Columns
    id = Column(Integer, primary_key=True, index=True)  # Primary Key
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    slug = Column(String, unique=True, index=True)

    # Relationships
    user = relationship("User", back_populates="tasks")  # Use string "User"
