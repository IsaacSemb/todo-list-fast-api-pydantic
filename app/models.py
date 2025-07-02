
from datetime import datetime, timezone
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.database import Base

def get_current_utc():
    """
    Return current UTC datetime with timezone info.
    """
    return datetime.now(timezone.utc)

class Todo(Base):
    """
    SQLAlchemy ORM model for the todos table.
    This is the database-facing model.
    """
    __tablename__ = "todos"
    
    id = sa.Column(sa.Integer, primary_key=True, index=True)
    title = sa.Column(sa.String(255), nullable=False)
    description = sa.Column(sa.Text)
    expected_completion = sa.Column(sa.DateTime, nullable=True)
    status = sa.Column(sa.Boolean, default=False)
    created_at = sa.Column(sa.DateTime(timezone=True), default=get_current_utc, nullable=False)
    updated_at = sa.Column(sa.DateTime(timezone=True), default=get_current_utc, onupdate=get_current_utc, nullable=False)
    
    
    # foreign key to users table
    #  CASCADE mean if user is deleted, delete the todos too
    user_id = sa.Column(sa.Integer, sa.ForeignKey(column='users.id', ondelete="CASCADE"))
    
    # internal ORM relation between user and todos
    owner = so.relationship('User', back_populates='todos')


class User(Base):
    """
    SQLAlchemy ORM model for the users table.
    This is the database facing model for users of the system.
    """
    
    __tablename__ = "users"

    id = sa.Column(sa.Integer, primary_key=True, index=True)
    username = sa.Column(sa.String, unique=True, index=True, nullable=False)
    email = sa.Column(sa.String, unique=True, index=True, nullable=False)
    hashed_password = sa.Column(sa.String, nullable=False)
    
    
    # internal ORM relation between todos and user
    todos = so.relationship('Todo', back_populates='owner')
