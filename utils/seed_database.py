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

from app.database import SessionLocal
from app.models import Todo
def get_json_data(file):
    
    file_path = os.path.join(basedir, file)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data

data = get_json_data('todo_fake_data.json') 

db = SessionLocal()
print(db)

print(data[0])
# sys.exit()

db.add(Todo())
db.commit()
db.close()