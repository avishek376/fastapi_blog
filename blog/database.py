from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLAlchemy for database operations in FastAPI for relational databases

sqlalchemy_db_url = 'sqlite:///./blog.db'  # SQLite database URL

# Create a SQLAlchemy engine
engine = create_engine(sqlalchemy_db_url, connect_args={"check_same_thread": False}, echo=True)

# Create a session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class
Base = declarative_base()
