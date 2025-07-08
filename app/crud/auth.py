from typing import List, Optional
from fastapi import HTTPException
from app import models
from app import schemas
from sqlalchemy.orm import Session

from app.core import security


def create_user( db: Session, user_data: schemas.UserCreate ) -> schemas.UserInDB:
   """
   Persist a new user object in the database.  

   Args:
      db (Session): SQLAlchemy database session.  
      user_data (userCreate): Data to create the user object.  
   
   On top of which, this call a helper to hash the password too  
   before persisting it to the database

   Returns:
      models.User: The created and persisted user object.
   """
   
   # get the password from the user data and hash it
   hashed_pw = security.hash_password(user_data.password)
   
   # create the user db object using the hashed password 
   db_user = models.User(
      username=user_data.username,
      email=user_data.email,
      hashed_password=hashed_pw
   )
   
   # add the user and commit the changes to the database
   db.add(db_user)
   db.commit()
   
   # refresh the database to get freshest changes from the database (eg tokens)
   db.refresh(db_user)
   
   # return the newly created user object
   return db_user



def get_user( db: Session, user_id: int ) -> Optional[schemas.UserResponse]:
   """
   Retrieve a user object by ID.

   Args:
      db (Session): SQLAlchemy database session.
      user_id (int): ID of the user object.

   Returns:
      models.User: The user object if found.

   Raises:
      HTTPException: If the object is not found.
   """
   user = db.query(models.User).filter(models.User.id == user_id).first()
   if not user:
      raise HTTPException(status_code=404, detail="user not found")
   return user



def list_users( db: Session, skip: int = 0, limit: int = 10 ):
   """
   Retrieve a list of user objects using pagination.

   Args:
      db (Session): SQLAlchemy database session.
      skip (int): Number of records to skip.
      limit (int): Number of records to return.

   Returns:
      List[models.User]: List of user objects.
   """
   return db.query(models.User).offset(skip).limit(limit).all()



def update_user( db: Session, user_id: int, user_update: schemas.UserUpdate ) -> Optional[schemas.UserResponse]:
   """
   Update an existing user object.

   Args:
      db (Session): SQLAlchemy database session.
      user_id (int): ID of the user object to update.
      user_update (schemas.UserUpdate): Data to update.

   Returns:
      models.User: The updated user object.

   Raises:
      HTTPException: If the object is not found.
   """
   user_object = db.query(models.User).filter(models.User.id == user_id).first()
   
   if not user_object:
      raise HTTPException(status_code=404, detail="user not found")
   
   update_data = user_update.model_dump(exclude_unset=True)
   
   for key, value in update_data.items():
      setattr(user_object, key, value)
   
   db.commit()
   db.refresh(user_object)
   
   return user_object



def delete_user( db: Session, user_id: int ) -> Optional[schemas.UserResponse]:
   """
   Delete a user object from the database.

   Args:
      db (Session): SQLAlchemy database session.
      user_id (int): ID of the user object to delete.

   Returns:
      None

   Raises:
      HTTPException: If the object is not found.
   """
   user = db.query(models.User).filter(models.User.id == user_id).first()
   
   if not user:
      raise HTTPException(status_code=404, detail="user not found")
   
   db.delete(user)
   db.commit()
   # return user
   return




