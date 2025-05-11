
# python imports
from datetime import datetime
from typing import List, Optional

# fastapi imports
from fastapi import APIRouter

# personal imports
from todos.schemas import ToDo, ToDoCreate, ToDoUpdate



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
@router.post('/',response_model=ToDo)
def create_todo( todo: ToDoCreate ) -> ToDoCreate:
    pass

# Retrieve single todo Item by id
@router.get('/{todo_id}', response_model=ToDo)
def get_todo(todo_id: int) -> Optional[ToDo]:
    pass

# Retrieve all todo Items 
# TODO: Incoperate pagination of some sort
@router.get('/', response_model=List[ToDo])
def list_todos() -> List[ToDo]:
    pass



# Updating a Todo Item 
@router.put('/{todo_id}', response_model=None) 
def update_todo(todo_id: int, todo_update:ToDoUpdate) -> ToDo:
    pass


# Deleting a todo Item
@router.delete('/{todo_id}')
def delete_todo(todo_id: int) -> None:
    pass
