import json
from pprint import pprint
import sys
import os

# home directory for this script
basedir = os.path.abspath(os.path.dirname(__file__))

# root diretory for the project
root_dir = os.path.abspath(os.path.dirname(basedir))

print(basedir)
print(root_dir)

# Add to sys.path
if root_dir not in sys.path:
    sys.path.append(root_dir)

from app import database, crud, schemas

def get_json_data(file):
    
    file_path = os.path.join(basedir, file)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data

data = get_json_data('todo_fake_data.json') 

db = database.SessionLocal()

print(db)

notes = """

🧪 TESTING Pydantic + CRUD

In FastAPI routes, validation is automatic via Pydantic.

But in tests and scripts, I must **manually** instantiate the schema:
    todo = TodoCreate(**data)

This ensures that the data passed to CRUD functions is validated
the same way it would be in production routes.

✅ Always use Pydantic models manually in tests.

"""


def testing_database_reset():
    
    data = {
            "title": "Learn FastAPI",
            "description": "Keep pushing!",
            "expected_completion": "2025-04-12T10:00:00",
            "status": False
            }
    
    crud.reset_database( engine= database.db_engine )

    sample_todo = schemas.ToDoCreate(**data)
    # print(sample_todo)
    crud.create_todo(db, sample_todo)
    

testing_database_reset()

