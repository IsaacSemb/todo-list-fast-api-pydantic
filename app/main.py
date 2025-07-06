# fast api
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# project context imports
from app import routes

from app.database import db_engine
from fastapi.responses import RedirectResponse

from app.models import todos

# create app from fast api
# run the server with 
# uvicorn main:app --reload
# uvicorn src.main:app --reload
app = FastAPI()

# use the base to create the database
todos.Base.metadata.create_all(bind=db_engine)


# register routers
app.include_router(routes.router, prefix='/api/v1/todos', tags=['Todos'] )


# Landing route 
@app.get('/', response_class=HTMLResponse, tags=['Home Health Check']) 
def home():
    """
    This endpoint is for testing server health
    """
    return RedirectResponse(url="/docs")