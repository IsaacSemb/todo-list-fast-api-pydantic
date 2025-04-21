# fastapi imports
from fastapi import APIRouter

# sql alchemy imports
from sqlalchemy.orm import Session

# personal imports
from src.database_crud import create_todo, get_todo, get_todos, update_todo, delete_todo
from src.schemas.todo_schemas1 import ToDoResponse, ToDoCreate, ToDoUpdate
# from database.database_configuration 

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
@router.post('/',response_model=ToDoResponse)
def create_todo():
    pass


@router.get('/', response_model=list[ToDoResponse])
def get_all_todos():
    pass

# Retrieve single todo Item by id
@router.get('/{todo_id}', response_model=ToDoResponse)
def get_todo():
    pass

# Updating a Todo Item 
@router.put('/{todo_id}', response_model=None) 
def update_todo(todo_id: int, todo_update:ToDoUpdate):
    pass


# Deleting a todo Item
@router.delete('/{todo_id}', response_model=ToDoResponse)
def delete_todo(todo_id: int):
    pass