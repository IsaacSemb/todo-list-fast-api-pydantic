
from datetime import datetime, timezone
import sqlalchemy as sa
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

