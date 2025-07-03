
import secrets
from passlib.context import CryptContext


# pwd_context is a Passlib CryptContext instance used to hash and verify passwords securely.
# It manages hashing algorithms and settings, making password management safer and easier.
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    """
    Hashes a plain-text password using the configured password context.
    Args:
        password (str): The plain-text password to hash.
    Returns:
        str: The hashed password.
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifies that a plain text password matches its hashed version.
    Args:
        plain_password (str): The plain text password provided by the user.
        hashed_password (str): The hashed password stored in the database.
    Returns:
        bool: True if the plain password matches the hashed password, False otherwise.
    """
    return pwd_context.verify(plain_password, hashed_password)