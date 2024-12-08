from sqlalchemy.orm import DeclarativeBase  # Modern DeclarativeBase for SQLAlchemy 2.x
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Database URL for SQLite
DATABASE_URL = "sqlite:///taskmanager.db"

# Create the database engine
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base class for models
class Base(DeclarativeBase):  # Use DeclarativeBase for SQLAlchemy 2.x
    pass
