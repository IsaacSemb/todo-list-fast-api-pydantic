
# fast api
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# python standard library
from typing import List
from datetime import datetime

# personal
from models import ToDoCreate, ToDo
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
    pass

@app.delete('/todos/{todo_id}', response_model=ToDo)
def delete_todo(todo_id: int):
    pass

@app.put('/todos/{todo_id}', response_model=ToDo)
def update_todo(todo_id: int):
    pass