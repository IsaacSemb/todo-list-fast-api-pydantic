
from fastapi import FastAPI
from typing import List
from models import ToDoCreate, ToDo
from datetime import datetime

import os
import json


# create app from fast api
# run the server with 
# uvicorn main:app --reload
app = FastAPI()


# temporary database for our todos ( DEPRACATED REAL FAST LOL )
todos: List[ToDo] = []



# incooperating persistence into the app

TODO_STORAGE_FILE = 'todo_db.json'


def load_todos() -> List[ToDo]:
    
    # check if the storage exists
    if not os.path.exists(TODO_STORAGE_FILE):
        return []
    
    with open(TODO_STORAGE_FILE, 'r') as f:
        
        try:
            data = json.load(f)
            return [ ToDo(**item) for item in data ]
        
        except json.JSONDecodeError:
            print('Encountered error parsing storage')
            return []

def save_todos(todos: List[ToDo]) -> None:
    
    with open(TODO_STORAGE_FILE, 'w') as f:
        
        # convert all todos from pydantic format to normal dicts before dumping
        data = [ todo.model_dump(mode='json') for todo in todos ]
        print(data)
        json.dump(data, f, indent=2)

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