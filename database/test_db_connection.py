from sqlalchemy import text
from database.db_config import db_engine

try:
    with db_engine.connect() as connection:
        result = connection.execute(text('SELECT 1'))
        print("connection sucessful:", result.scalar())
except Exception as e:
    print("connection failed: ", e)
    
