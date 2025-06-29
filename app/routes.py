
# python imports
from datetime import datetime
from typing import List, Optional

# fastapi imports
from fastapi import APIRouter, Depends, HTTPException

# sql alchemy imports
from sqlalchemy.orm import Session

# personal imports
from app.database import get_db
from app.schemas import ToDoCreate, ToDoResponse, ToDoUpdate
from app import models


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
@router.post('/', response_model=ToDoResponse)
def create_todo( todo_data: ToDoCreate, db: Session = Depends(get_db) ) -> ToDoCreate:
    todo_item = models.Todo(**todo_data.model_dump())
    db.add(todo_item)
    db.commit()
    db.refresh(todo_item)
    return todo_item
    

# Retrieve single todo Item by id
@router.get('/{todo_id}', response_model=ToDoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db) ) -> Optional[ToDoResponse]:
    
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo Item not found")
    return todo

# Retrieve all todo Items 
@router.get('/', response_model=List[ToDoResponse])
def list_todos(db: Session = Depends(get_db), skip: int = 0, limit: int = 10 ):
    return db.query(models.Todo).offset(skip).limit(limit).all()


# Updating a Todo Item 
@router.put('/{todo_id}', response_model=ToDoResponse) 
def update_todo(todo_id: int, todo_update: ToDoUpdate, db: Session = Depends(get_db)) -> Optional[ToDoResponse]:
    
    todo_item = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    
    if not todo_item:
        raise HTTPException(status_code=404, detail="Todo Item not found")

    update_data = todo_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(todo_item, key, value)

    db.commit()
    db.refresh(todo_item)
    return todo_item


# Deleting a todo Item
@router.delete('/{todo_id}', status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db)) -> None:
    
    todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
    
    if not todo:
        raise HTTPException(status_code=404, detail="Todo Item not found")
    
    db.delete(todo)
    db.commit()
    return
