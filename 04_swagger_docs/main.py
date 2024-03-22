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

# Define a route
@app.put("/{item_id}")
async def put_root(item_id: int):
    return {"message": f"Item ID is {item_id}"}