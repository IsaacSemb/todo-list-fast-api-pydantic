
# fast api
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.exceptions import HTTPException

# python standard library
from typing import List
from datetime import datetime

# personal
from models import ToDoCreate, ToDo, ToDoUpdate
from db_utils import load_todos, save_todos

# create app from fast api
# run the server with 
# uvicorn main:app --reload
app = FastAPI()


# temporary database for our todos ( DEPRACATED REAL FAST LOL )
todos: List[ToDo] = []

# new list pulls from file
todos: List[ToDo] = load_todos()


# Landing route 
@app.get('/', response_class=HTMLResponse)
def home():
    
    return '<h1>Welcome to FastAPI</h1>'
    return { 'message':'Welcome to fastAPI!' }

@app.post('/todos',response_model=ToDo)
def create_todo( todo: ToDoCreate ):
    
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

@app.get('/todos', response_model=List[ToDo])
def get_all_todos():
    return load_todos()


@app.get('/todos/{todo_id}', response_model=ToDo)
def get_todo(todo_id: int):
    todos = load_todos()
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail='ToDo not found')


@app.delete('/todos/{todo_id}')
def delete_todo(todo_id: int):
    todos = load_todos()
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            save_todos(todos)
            return {'message':"ToDo Deleted", 'details': todo }
    raise HTTPException(status_code=404, detail='ToDo not found')

@app.put('/todos/{todo_id}', response_model=None) 
def update_todo(todo_id: int, todo_update:ToDoUpdate):
    todos = load_todos()
    for todo in todos:
        
        if todo.id == todo_id: 
            old_todo = todo
        
            if todo_update.title is not None:
                todo.title = todo_update.title
        
            if todo_update.description is not None:
                todo.description = todo_update.description
        
            if todo_update.expected_completion is not None:
                todo.expected_completion = todo_update.expected_completion
        
            if todo_update.status is not None:
                todo.status = todo_update.status
        
            # save changes
            save_todos(todos)
        
            return {
                'message':'ToDo Updated',
                'old_todo':old_todo,
                'new_todo':todo
            }
    raise HTTPException(status_code=404, detail='ToDo not found') 

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