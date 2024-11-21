import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy.schema import CreateTable

# Create the engine with SQLite database
engine = create_engine('sqlite:///taskmanager.db', echo=True)

# Create session local for database operations
SessionLocal = sessionmaker(bind=engine)

# Create a base class for models
class Base(DeclarativeBase):
    pass

# Ensure models are imported only in the main block
if __name__ == "__main__":
    from app.models import user, task
    print(CreateTable(user.User.__table__).compile(engine))
    print(CreateTable(task.Task.__table__).compile(engine))
