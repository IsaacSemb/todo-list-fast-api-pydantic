
# python imports
from datetime import datetime
from typing import Any, List, Optional

# fastapi imports
from fastapi import APIRouter, Depends, HTTPException

# sql alchemy imports
from sqlalchemy.orm import Session

# personal imports
from app.database import get_db
from app import schemas
from app import crud, models


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
@router.post('/', response_model=schemas.ToDoResponse)
def create_todo( todo_data: schemas.ToDoCreate, db: Session = Depends(get_db) ) -> Any:
    return crud.create_todo( db, todo_data )

# Retrieve single todo Item by id
@router.get('/{todo_id}', response_model=schemas.ToDoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db) ) -> Optional[schemas.ToDoResponse]:
    return crud.get_todo( db, todo_id )

# Retrieve all todo Items 
@router.get('/', response_model=List[schemas.ToDoResponse])
def list_todos(db: Session = Depends(get_db), skip: int = 0, limit: int = 10 ):
    return crud.list_todos(db, skip, limit)

# Updating a Todo Item 
@router.put('/{todo_id}', response_model=schemas.ToDoResponse) 
def update_todo(todo_id: int, todo_update: schemas.ToDoUpdate, db: Session = Depends(get_db)) -> Optional[schemas.ToDoResponse]:
    return crud.update_todo(db, todo_id, todo_update)

# Deleting a todo Item
@router.delete('/{todo_id}')
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> Optional[schemas.ToDoResponse]:
    return crud.delete_todo(db, todo_id)
    