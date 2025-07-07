
# python imports
from datetime import datetime
from typing import Any, List, Optional

# fastapi imports
from fastapi import APIRouter, Depends, HTTPException

# sql alchemy imports
from sqlalchemy.orm import Session

# personal imports
from app.database import get_db
from app.schemas import todos
from app.crud import todos
from app.models import todos


# TODOS
# Add case-insensitive search or fuzzy matching
# Add logging instead of print
# Add caching if reading the file becomes too frequent
# Want to sort the todos? (e.g. newest first, or by status)
# Want to filter only completed / pending?
# Want to paginate large lists (e.g. ?limit=10&skip=20)?
# create a frontend with jinja
    # this is call for making a pluggable API for any front end to use
#  versioning of the apis 

# i keep seeing repetion in the routes to load the todos
# loop them and find the id NEED to change that
# change the update format too many if statements, that cant be optimal what if 100 attributes
# consider doing a model that changes only status 

router = APIRouter()

# Create a new todo Item
@router.post(
    '/', 
    response_model=todos.ToDoResponse,
    summary="Create a new Todo item",
    description="Creates a new Todo item using the provided data. Returns the created item with its assigned ID."
    )
def create_todo( todo_data: todos.ToDoCreate, db: Session = Depends(get_db) ) -> Any:
    """
    Create a new Todo item.

    This delegates the actual creation logic to the CRUD layer,  
    which handles database insertion and model serialization.

    Args:
        todo_data (schemas.ToDoCreate): The input payload for the new Todo.  
        db (Session): Database session dependency.

    Returns:
        schemas.ToDoResponse: The newly created Todo item.
    """
    return todos.create_todo( db, todo_data )



# Retrieve single todo Item by id
@router.get(
    '/{todo_id}',
    response_model=todos.ToDoResponse,
    summary="Get a Todo item by ID",
    description="Retrieves a specific Todo item by its unique ID. Returns a 404 error if the item does not exist."
    )
def get_todo(todo_id: int, db: Session = Depends(get_db) ) -> Optional[todos.ToDoResponse]:
    """
    Retrieve a Todo item by its ID.

    This delegates the lookup and error handling to the CRUD layer,  
    which returns the item or raises a 404 error if not found.

    Args:
        todo_id (int): The ID of the Todo to retrieve.
        db (Session): Database session dependency.

    Returns:
        schemas.ToDoResponse: The requested Todo item.
    """
    return todos.get_todo( db, todo_id )



# Retrieve all todo Items 
@router.get(
    '/',
    response_model=List[todos.ToDoResponse],
    summary="List all Todo items",
    description="Retrieves a list of Todo items with optional pagination using 'skip' and 'limit' query parameters."
    )
def list_todos(db: Session = Depends(get_db), skip: int = 0, limit: int = 10 ):
    """
    List all Todo items with optional pagination.

    This route forwards pagination parameters to the CRUD layer,  
    which retrieves and returns the relevant Todo records.

    Args:
        db (Session): Database session dependency.
        skip (int): Number of records to skip.
        limit (int): Max number of records to return.

    Returns:
        List[schemas.ToDoResponse]: A list of Todo items.
    """
    return todos.list_todos(db, skip, limit)



# Updating a Todo Item 
@router.put(
    '/{todo_id}',
    response_model=todos.ToDoResponse,
    summary="Update a Todo item",
    description="Updates an existing Todo item with the provided fields. Returns the updated item, or 404 if not found."
    ) 
def update_todo(todo_id: int, todo_update: todos.ToDoUpdate, db: Session = Depends(get_db)) -> Optional[todos.ToDoResponse]:
    """
    Update an existing Todo item.

    The update operation is delegated to the CRUD layer,  
    which handles field updates, validation, and missing record checks.

    Args:
        todo_id (int): ID of the Todo to update.
        todo_update (schemas.ToDoUpdate): Fields to be updated.
        db (Session): Database session dependency.

    Returns:
        schemas.ToDoResponse: The updated Todo item.
    """
    return todos.update_todo(db, todo_id, todo_update)



# Deleting a todo Item
@router.delete(
    '/{todo_id}',
    response_model=None,
    summary="Delete a Todo item",
    description="Deletes the specified Todo item by ID. Returns a 404 error if the item does not exist."
    )
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> Optional[todos.ToDoResponse]:
    """
    Delete a Todo item by ID.

    This route delegates deletion to the CRUD layer,  
    which removes the item from the database and handles not-found cases.

    Args:
        todo_id (int): ID of the Todo to delete.
        db (Session): Database session dependency.

    Returns:
        None: If successful, the item is deleted. Otherwise, an exception is raised.
    """
    return todos.delete_todo(db, todo_id)
    