
# This file is for pydantic models for structuring how data will look like

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


# this model is for user entry
class ToDoCreate(BaseModel):    
    title: str
    description: Optional[str] = None
    expected_completion: Optional[datetime] = None

# this is a server side model
class ToDo(BaseModel):
    id : int
    title: str
    description: Optional[str] = None
    created_at: datetime
    expected_completion: Optional[datetime] = None
    status: bool = False 

# a todo model for incomming updates
class ToDoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    expected_completion: Optional[datetime] = None
    status: Optional[bool] = None 