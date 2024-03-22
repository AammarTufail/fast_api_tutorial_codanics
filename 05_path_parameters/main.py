from fastapi import FastAPI

app = FastAPI() # Create an instance of FastAPI

# Define a route
@app.get("/")
async def root():
    return {"message": "Hello World we are learning on codanics.com"}

# Define a route
@app.post("/")
async def post_root():
    return {"message": "This is a POST request"}

# add a path parameter
@app.get("/items")
async def get_items():
    return {"message": "This route will list items"}

# add path parameter in the route items as item ids
@app.get("/items/{item_id}")
async def get_item(item_id: str):
    return {"item_id": item_id}

@app.get("/users")
async def get_users():
    return {"message": "This route will list userss"}

# same path parametere for user
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    return {"user_id": user_id}