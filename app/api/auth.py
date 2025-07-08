# type: ignore
"""
This started out as user

And i used standard CRUD like 
create user
read users
update users
delete user

But from standards
users is whats drive authentication hemce why its called auth 

and its endpoints and contribution to the codebase is different from standard crud



"""

from datetime import datetime
from typing import Any, List, Optional
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app import crud, schemas

router = APIRouter()


@router.post(
    '/register',
    response_model=schemas.UserResponse,
    summary="Create a new user object",
    description="Register a new user object using the provided data to the system. Returns the created object with its assigned ID."
    )
def register( user_data: schemas.UserCreate, db: Session = Depends(get_db) ) -> Any:
    """
    Create a new user object to be registered to the system.

    This delegates the actual creation logic to the CRUD layer,  
    which handles database insertion and model serialization.

    Args:
        user_data (schemas.UserCreate): The input payload for the new user.  
        db (Session): Database session dependency.

    Returns:
        schemas.UserResponse: The newly created user object.
    """
    return crud.create_user( db, user_data )



# Retrieve single todo object by id
@router.post(
    '/login',
    response_model=schemas.Token,
    summary="This action logins in the user",
    description="This returns an access token for user to be able to login"
    )
def login( input: schemas.LoginInput, db: Session = Depends(get_db) ):
    """
    Handles user login by verifying credentials and generating an authentication token.  
    Args:  
        input (LoginInput): The user's login credentials, including email and password.  
        db (Session, optional): The database session dependency.  
    Returns:  
        dict: A dictionary containing the access token (JWT) and the token type ("bearer").  
    This function is used when a user logs in. It authenticates the user and creates a JWT access token, which is returned along with the token type ("bearer").  
    """
    return crud.login_user(input.email, input.password) 












































































# Retrieve all todo objects 
@router.get(
    '/',
    response_model=List[schemas.UserResponse],
    summary="List all user objects",
    description="Retrieves a list of user objects with optional pagination using 'skip' and 'limit' query parameters."
    )
def list_users(db: Session = Depends(get_db), skip: int = 0, limit: int = 10 ):
    """
    List all user objects with optional pagination.

    This route forwards pagination parameters to the CRUD layer,  
    which retrieves and returns the relevant user records.

    Args:
        db (Session): Database session dependency.
        skip (int): Number of records to skip.
        limit (int): Max number of records to return.

    Returns:
        List[schemas.UserResponse]: A list of user objects.
    """
    return crud.list_users(db, skip, limit)



# Updating a user object 
@router.put(
    '/{user_id}',
    response_model=schemas.UserResponse,
    summary="Update a user object",
    description="Updates an existing user object with the provided fields. Returns the updated object, or 404 if not found."
    ) 
def update_user(user_id: int, user_update: schemas.UserUpdate, db: Session = Depends(get_db)) -> Optional[schemas.UserResponse]:
    """
    Update an existing user object.

    The update operation is delegated to the CRUD layer,  
    which handles field updates, validation, and missing record checks.

    Args:
        user_id (int): ID of the user to update.
        user_update (schemas.UserUpdate): Fields to be updated.
        db (Session): Database session dependency.

    Returns:
        schemas.UserResponse: The updated user object.
    """
    return crud.update_user(db, user_id, user_update)



# Deleting a todo object
@router.delete(
    '/{user_id}',
    response_model=None,
    summary="Delete a user object",
    description="Deletes the specified user object by ID. Returns a 404 error if the object does not exist."
    )
def delete_user(user_id: int, db: Session = Depends(get_db)) -> Optional[schemas.UserResponse]:
    """
    Delete a user object by ID.

    This route delegates deletion to the CRUD layer,  
    which removes the object from the database and handles not-found cases.

    Args:
        user_id (int): ID of the user to delete.
        db (Session): Database session dependency.

    Returns:
        None: If successful, the object is deleted. Otherwise, an exception is raised.
    """
    return crud.delete_user(db, user_id)
    