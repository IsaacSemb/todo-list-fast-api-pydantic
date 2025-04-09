import os
import json
from typing import List
from models import ToDo

TODO_STORAGE_FILE = 'todo_db.json'


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

    with open(TODO_STORAGE_FILE, 'r') as f:

        try:
            data = json.load(f)
            return [ ToDo(**item) for item in data ]

        except json.JSONDecodeError:
            print('Encountered error parsing storage')
            return []