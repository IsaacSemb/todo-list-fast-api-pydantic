
import sqlalchemy as sa
import sqlalchemy.orm as so
from app.database import Base
from app.models.utils import get_current_utc

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


