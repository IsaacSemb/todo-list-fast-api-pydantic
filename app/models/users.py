from app.database import Base
from app.models.utils import get_current_utc


import sqlalchemy as sa
import sqlalchemy.orm as so


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
    created_at = sa.Column(sa.DateTime(timezone=True), default=get_current_utc, nullable=False)
    updated_at = sa.Column(sa.DateTime(timezone=True), default=get_current_utc, onupdate=get_current_utc, nullable=False)


    # internal ORM relation between todos and user
    todos = so.relationship('Todo', back_populates='owner')