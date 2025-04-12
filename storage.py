from typing import List
from db_utils import load_todos
from models import ToDo


from fastapi.exceptions import HTTPException

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