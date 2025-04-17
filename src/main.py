# fast api
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

# project context imports
from src.routes.todos import router as todos_router


# create app from fast api
# run the server with 
# uvicorn main:app --reload
app = FastAPI()

# register routers
app.include_router(todos_router, prefix='/api', tags=['Todos','semb-todos'] )


# Landing route 
@app.get('/', response_class=HTMLResponse) 
def home():
    # return { 'message':'Welcome to fastAPI!' }
    return '<h1>Welcome to my FastAPI ToDo API</h1>'