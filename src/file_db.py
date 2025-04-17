
# python imports
import os
import json
from typing import List

# personal imports
from src.schemas.todo_schemas import ToDo

# fast api imports
from fastapi.exceptions import HTTPException


ROOT_DIR = os.path.dirname( os.path.dirname(__file__) )
TODO_STORAGE_FILE = os.path.join(ROOT_DIR, 'db/todo_db.json' )



# to write todos to file db
def save_todos(todos: List[ToDo]) -> None:

    with open(TODO_STORAGE_FILE, 'w') as f:

        # convert all todos from pydantic format to normal dicts before dumping
        data = [ todo.model_dump(mode='json') for todo in todos ]
        json.dump(data, f, indent=2)


# to read todos from db
def load_todos() -> List[ToDo]:

    # check if the storage exists
    if not os.path.exists(TODO_STORAGE_FILE):
        return []

    with open(TODO_STORAGE_FILE, 'r', encoding='utf-8') as f:  

        try:
            data = json.load(f)
            return [ ToDo(**item) for item in data ]

        except json.JSONDecodeError:
            print('Encountered error parsing storage')
            return []
        
# helper function to find a todo
def get_todo_by_id(todo_id: int) -> ToDo:
    todos = load_todos()
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail='ToDo Not Found')

# helper function to find a todo by its index in entire list
def get_todo_index_by_todo_id( todo_id: int, todos: List[ToDo] ) -> int:

    for idx, todo_item in enumerate(todos):
        if todo_item.id == todo_id:
            return idx

    raise HTTPException(status_code=404, detail='ToDo Not Found')