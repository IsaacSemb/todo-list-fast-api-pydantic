
from fastapi import FastAPI
from typing import List
from datetime import datetime


from models import ToDoCreate, ToDo
from db_utils import load_todos, save_todos



# create app from fast api
# run the server with 
# uvicorn main:app --reload
app = FastAPI()


# temporary database for our todos ( DEPRACATED REAL FAST LOL )
todos: List[ToDo] = []



# incooperating persistence into the app



# new list pulls from file
todos: List[ToDo] = load_todos()


# Landing route 
@app.get('/')
def home():
    
    print( load_todos() )
    
    return { 'message':'Welcome to fastAPI!' }

@app.post('/todos',response_model=ToDo)
def create_todo( todo: ToDoCreate ):
    
    new_todo_item = ToDo(
        id=len(todos)+1,
        title=todo.title,
        description=todo.description,
        expected_completion=todo.expected_completion,
        created_at=datetime.now(),
        status=False
    )
    
    todos.append(new_todo_item)
    
    save_todos(todos)
    
    return new_todo_item