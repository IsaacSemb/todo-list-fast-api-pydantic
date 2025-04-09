from fastapi import FastAPI
from typing import List
from models import ToDoCreate, ToDo
from datetime import datetime

# create app from fast api
# run the server with 
# uvicorn main:app --reload
app = FastAPI()



# temporary database for our todos
todos: List[ToDo] = []


# Landing route 
@app.get('/')
def home():
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
    
    return new_todo_item