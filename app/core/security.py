
from datetime import datetime, timedelta, timezone
import secrets
from passlib.context import CryptContext
from jose import jwt, JWTError


# Generate a secure random secret key (uncomment to use in production)
SECRET_KEY = "kachabali-XTRA" or secrets.token_urlsafe(32)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


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


#  ================= JWT STUFF ======================

# STANDARD JWT STUFF 
# 
# "iss" → issuer
# "sub" → subject (who it's about)
# "aud" → audience
# "exp" → expiration time
# "nbf" → not before
# "iat" → issued at

def create_access_token(data: dict, expires_in: timedelta | None = None):
    """
    this is a helper function to create a JWT token to use in auth flow
    """
    # make a copy of the data to encode in our case we have started with email
    data_to_encode = data.copy()
    
    # This is the full UTC aware period for the expiry of this token
    expiry_datetime = datetime.now(timezone.utc) + (expires_in or timedelta(minutes=30))
    
    # get the data to encode and add the expiry part to it 
    data_to_encode.update({"exp": expiry_datetime})
    
    # return the entire token with all the good stuff 
    # like data and expiry 
    return jwt.encode(data_to_encode, SECRET_KEY, algorithm=ALGORITHM)

def decode_access_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        return None