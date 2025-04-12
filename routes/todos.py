
# python imports
from datetime import datetime
from typing import List

# fastapi imports
from fastapi import APIRouter

# personal imports
from file_db import load_todos, save_todos, get_todo_by_id, get_todo_index_by_todo_id
from models import ToDo, ToDoCreate, ToDoUpdate


# TODOS
# Add case-insensitive search or fuzzy matching
# Add logging instead of print
# Add caching if reading the file becomes too frequent
# Want to sort the todos? (e.g. newest first, or by status)
# Want to filter only completed / pending?
# Want to paginate large lists (e.g. ?limit=10&skip=20)?
# create a frontend with jinja

# i keep seeing repetion in the routes to load the todos
# loop them and find the id NEED to change that
# change the update format too many if statements, that cant be optimal what if 100 attributes
# consider doing a model that changes only status


router = APIRouter()

# new list pulls from file
todos: List[ToDo] = load_todos()

@router.get('/todos/{todo_id}', response_model=ToDo)
def get_todo(todo_id: int):
    return get_todo_by_id(todo_id)

@router.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    todos_list = load_todos()
    target_todo_index = get_todo_index_by_todo_id(todo_id=todo_id, todos=todos_list)    
    deleted_todo = todos_list.pop(target_todo_index)
    save_todos(todos_list)
    return {'message':"ToDo Deleted", 'details': deleted_todo }
    
@router.put('/todos/{todo_id}', response_model=None) 
def update_todo(todo_id: int, todo_update:ToDoUpdate):
    todos = load_todos()
    target_todo_index: ToDo = get_todo_index_by_todo_id(todo_id,todos)
    target_todo = todos[target_todo_index]
    
    old_todo = target_todo.model_copy(deep=True)
    
    # consider putting this in a helper function
    if todo_update.title is not None:
        target_todo.title = todo_update.title

    if todo_update.description is not None:
        target_todo.description = todo_update.description

    if todo_update.expected_completion is not None:
        target_todo.expected_completion = todo_update.expected_completion

    if todo_update.status is not None:
        target_todo.status = todo_update.status

    # save changes
    save_todos(todos)
        
    return {
        'message':'ToDo Updated',
        'old_todo':old_todo,
        'new_todo':target_todo
    }
    
    
@router.post('/todos',response_model=ToDo)
def create_todo( todo: ToDoCreate ):
    
    todos = load_todos()
    
    new_todo_item = ToDo(
        id = len(todos)+1,
        title = todo.title,
        description = todo.description,
        expected_completion = todo.expected_completion,
        created_at = datetime.now(),
        status = False
    )
    todos.append(new_todo_item)
    save_todos(todos)
    return new_todo_item

@router.get('/todos', response_model=List[ToDo])
def get_all_todos():
    return load_todos()