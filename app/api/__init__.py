from fastapi import APIRouter
from .todos import router as todos_router
# from .users import router as users_router

router = APIRouter()

router.include_router(todos_router, prefix="/api/v1/todos", tags=["Todos"])
# router.include_router(users_router, prefix="/users", tags=["Users"])
