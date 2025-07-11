"""
CRUD operations for Todo items.

This module provides low-level database access functions for creating, reading, updating,
and deleting Todo items using SQLAlchemy ORM.

Each function receives a database session and performs direct DB operations. 
Some functions also handle basic validation (e.g., checking for existence and raising HTTPExceptions).

Note:
   These functions are invoked by the API route handlers and are not intended to be used directly 
   by external clients. They assume valid input from upstream and may raise HTTPException
   for not-found cases.

Responsibilities:
   - Map Pydantic models to SQLAlchemy models
   - Execute SQLAlchemy queries
   - Commit changes to the database
   - Handle 404 logic for missing records (as part of API integration)

If more complex business logic is needed, consider adding a separate service layer.
"""

from typing import List, Optional

from fastapi import HTTPException
from app import models
from app import schemas
from sqlalchemy.orm import Session

notes = """

🧠 PERSONAL REVELATION — WHY CRUD LOGIC MUST BE SEPARATE FROM ROUTES

I didn’t fully understand why logic was moved out of FastAPI routes and into a `crud.py` file,
until I faced a real limitation:

I wanted to insert data into my database directly (e.g., via a script, not by calling an API route).
But because all my DB logic was embedded inside route functions, I couldn't access it without
running the entire FastAPI server.

💡 That's when it clicked: keeping logic in `crud.py` makes it reusable — I can call it from:
   - API routes
   - CLI scripts
   - unit tests
   - startup events
   - background tasks

Trying to bypass the API made me understand that logic tied to HTTP routes is not reusable logic.

Now I see:
> ROUTES = glue between the outside world and internal logic  
> CRUD = the actual logic that can be used anywhere

This is more than a coding style — it's a foundation for maintainable, testable software.


🧠 TECHNICAL: WHY THIS crud.py FILE EXISTS

The purpose of this module is to separate business logic (e.g., database operations)
from the route definitions (i.e., API endpoints).

This achieves several things:
1. REUSABILITY — The same logic can be reused from:
   - FastAPI routes
   - CLI scripts
   - startup/shutdown events
   - unit tests
   - background jobs

2. TESTABILITY — You can write focused unit tests for the logic here
   without needing to spin up the entire FastAPI app.

3. DECOUPLING — Keeping logic out of route functions avoids tight coupling
   to the HTTP layer and encourages a cleaner, layered architecture.

4. CLARITY — Routes should just coordinate the flow: 
   receive input → call logic (from crud) → return result.

TL;DR:
Don’t put logic in your routes — put it here. Routes should delegate, not operate.
"""



def create_todo( db: Session, todo_data: schemas.ToDoCreate ) -> schemas.ToDoCreate:
   """
   Persist a new Todo item in the database.  

   Args:
      db (Session): SQLAlchemy database session.  
      todo_data (ToDoCreate): Data to create the Todo item.  

   Returns:
      models.Todo: The created and persisted Todo item.
   """
   todo_item = models.Todo(**todo_data.model_dump())
   db.add(todo_item)
   db.commit()
   db.refresh(todo_item)
   return todo_item



def get_todo( db: Session, todo_id: int ) -> Optional[schemas.ToDoResponse]:
   """
   Retrieve a Todo item by ID.

   Args:
      db (Session): SQLAlchemy database session.
      todo_id (int): ID of the Todo item.

   Returns:
      models.Todo: The Todo item if found.

   Raises:
      HTTPException: If the item is not found.
   """
   todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
   if not todo:
      raise HTTPException(status_code=404, detail="Todo Item not found")
   return todo



def list_todos( db: Session, skip: int = 0, limit: int = 10 ):
   """
   Retrieve a list of Todo items using pagination.

   Args:
      db (Session): SQLAlchemy database session.
      skip (int): Number of records to skip.
      limit (int): Number of records to return.

   Returns:
      List[models.Todo]: List of Todo items.
   """
   return db.query(models.Todo).offset(skip).limit(limit).all()



def update_todo( db: Session, todo_id: int, todo_update: schemas.ToDoUpdate ) -> Optional[schemas.ToDoResponse]:
   """
   Update an existing Todo item.

   Args:
      db (Session): SQLAlchemy database session.
      todo_id (int): ID of the Todo item to update.
      todo_update (schemas.ToDoUpdate): Data to update.

   Returns:
      models.Todo: The updated Todo item.

   Raises:
      HTTPException: If the item is not found.
   """
   todo_item = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
   
   if not todo_item:
      raise HTTPException(status_code=404, detail="Todo Item not found")
   
   update_data = todo_update.model_dump(exclude_unset=True)
   
   for key, value in update_data.items():
      setattr(todo_item, key, value)
   
   db.commit()
   db.refresh(todo_item)
   
   return todo_item



def delete_todo( db: Session, todo_id: int ) -> Optional[schemas.ToDoResponse]:
   """
   Delete a Todo item from the database.

   Args:
      db (Session): SQLAlchemy database session.
      todo_id (int): ID of the Todo item to delete.

   Returns:
      None

   Raises:
      HTTPException: If the item is not found.
   """
   todo = db.query(models.Todo).filter(models.Todo.id == todo_id).first()
   
   if not todo:
      raise HTTPException(status_code=404, detail="Todo Item not found")
   
   db.delete(todo)
   db.commit()
   # return todo
   return




