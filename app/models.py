from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Integer, String, Text
from app.database import Base

class Todo(Base):
    """
    SQLAlchemy ORM model for the todos table.
    This is the database-facing model.
    """
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    expected_completion = Column(Integer, nullable=True)  # epoch seconds
    status = Column(Boolean, default=False)
    created_at = Column(Integer, default=lambda: int(datetime.now(timezone.utc).timestamp()), nullable=False)  # epoch seconds
    updated_at = Column(Integer, default=lambda: int(datetime.now(timezone.utc).timestamp()), onupdate=lambda: int(datetime.now(timezone.utc).timestamp()), nullable=False)  # epoch seconds