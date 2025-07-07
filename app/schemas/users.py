from datetime import datetime
from pydantic import BaseModel


class UserBase(BaseModel):
    """
    Base schema for a user object.

    Defines the common fields shared by all user-related models.  
    Other user schemas should inherit from this class to ensure consistency.  
    Only extend or override this base model with clear justification.  
    """
    username: str
    email: str


class UserCreate(UserBase):
    """
    Schema for creating a new user object. Inherits all fields from UserBase.  
    Use this schema when creating a new user entry via API or form submission (sign Up).  
    """
    password: str


class UserUpdate(BaseModel):
    """
    Schema for updating an existing user item.
    I HAVENT YET FIGURED OUT IF THE USER SHOULD BE ALLOWED TO CHANGE ANYTHING
    """
    pass


class UserInDB(UserBase):
    """
    This is a system level contract that includes secret fields
    for keeping track of a user Object like the date of creation and update times  
    To maintain the integrity of the system   
    """
    id: int
    hashed_password: str
    created_at: datetime
    updated_at: datetime


class UserResponse(UserBase):
    """
    Represents the response schema for a user item, inheriting all fields from UserInDB.
    This class can be extended to add response-specific fields or documentation in the future.
    """
    class Config:
        orm_mode = True