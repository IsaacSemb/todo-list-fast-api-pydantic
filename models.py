
# This file is for pydantic models for structuring how data will look like

from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ToDoCreate(BaseModel):
    # this is a model for user input todos
    pass

class ToDo(BaseModel):
    # this is hoew a todo will look like serverside
    pass


