
# fast api
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# python standard library
from typing import List, Union
from datetime import datetime

# personal
from models import ToDoCreate, ToDo, ToDoUpdate
from file_db import load_todos, save_todos
from routes.todos import router as todos_router


# create app from fast api
# run the server with 
# uvicorn main:app --reload
app = FastAPI()

# register routers
app.include_router(todos_router)

# new list pulls from file
todos: List[ToDo] = load_todos()

# Landing route 
@app.get('/', response_class=HTMLResponse) 
def home():
    # return { 'message':'Welcome to fastAPI!' }
    return '<h1>Welcome to FastAPI</h1>'


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