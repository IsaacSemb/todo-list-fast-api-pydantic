
# This file is for pydantic models for structuring how data will look like
from pydantic import BaseModel
from typing import Optional
from datetime import datetime



# base model for all other models to use
class ToDoBase(BaseModel):
    """
    Base schema for a ToDo item.

    Defines the common fields shared by all ToDo-related models.  
    Other ToDo schemas should inherit from this class to ensure consistency.  
    Only extend or override this base model with clear justification.  
    """
    title: str
    description: Optional[str] = None
    expected_completion: Optional[datetime] = None
    status: bool= False 

# this model is for user entry
class ToDoCreate(ToDoBase):
    """
    Schema for creating a new ToDo item. Inherits all fields from ToDoBase.
    Use this schema when creating a new ToDo entry via API or form submission.
    """
    pass

# a todo model for acceptable incoming updates form the client
class ToDoUpdate(ToDoBase):
    """
    Schema for updating an existing ToDo item.
    Inherits all fields from ToDoBase. Use this class to validate and serialize data when updating ToDo entries.
    """
    pass


class ToDoInDB(ToDoBase):
    """
    This is a system level contract that includes secret fields  
    for keeping track of a todo like the date of creation and update times  
    To maintain the integrity of the system   
    """
    id: int
    created_at: datetime
    updated_at: datetime
    

# this is a server side model for returning data to the client
class ToDoResponse(ToDoInDB):
    """
    Represents the response schema for a ToDo item, inheriting all fields from ToDoInDB.
    This class can be extended to add response-specific fields or documentation in the future.
    """
    class Config:
        orm_mode = True 