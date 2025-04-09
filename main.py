from fastapi import FastAPI

# create app from fast api
app = FastAPI()

# create a route 

@app.get('/')
def home():
    return {'message': 'fastAPI first trial!'}


# run the server with 
# uvicorn main:app --reload
