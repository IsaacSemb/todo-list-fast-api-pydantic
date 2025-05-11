
from typing import List, Optional
from sqlalchemy.orm import Session
import models, schemas

"""
This module contains the actual CRUD (Create, Read, Update, Delete) functionality 
for managing todo items. It provides a set of helper functions that are utilized 
in the API routes to perform operations on todo items, such as creating new todos, 
retrieving existing ones, updating them, and deleting them.
Functions:
- create_todo: Creates a new todo item.
- get_todo: Retrieves a single todo item by its ID.
- list_todos: Retrieves all todo items (pagination to be incorporated in the future).
- update_todo: Updates an existing todo item by its ID.
- delete_todo: Deletes a todo item by its ID.
"""


def create_todo( db: Session, todo: schemas.ToDoCreate ) -> schemas.ToDoCreate:
    pass

# Retrieve single todo Item by id
def get_todo(todo_id: int) -> Optional[schemas.ToDo]:
    pass

# Retrieve all todo Items 
# TODO: Incoperate pagination of some sort
def list_todos() -> List[schemas.ToDo]:
    pass



# Updating a Todo Item 
def update_todo(todo_id: int, todo_update:schemas.ToDoUpdate) -> schemas.ToDo:
    pass


# Deleting a todo Item
def delete_todo(todo_id: int) -> None:
    pass
