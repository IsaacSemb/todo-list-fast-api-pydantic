
# This file is for pydantic models for structuring how data will look like
from pydantic import BaseModel
from typing import Optional
from datetime import datetime



# base model for a todo 
class ToDoBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    expected_completion: Optional[datetime] = None
    status: Optional[bool] = None 

# this model is for user entry
class ToDoCreate(ToDoBase):    
    created_at: datetime

# a todo model for acceptable incoming updates form the client
class ToDoUpdate(ToDoBase):
    pass
    
# this is a server side model for returning data
class ToDoResponse(ToDoBase):
    id : int