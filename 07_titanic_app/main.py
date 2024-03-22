from fastapi import FastAPI
import seaborn as sns
import pandas as pd

app = FastAPI() # Create a FastAPI instance

# Load the Titanic dataset
df = sns.load_dataset('titanic')

# perform a simple data transformation
survival_rate = df.groupby("class")["survived"].mean().reset_index()

# Define a route
@app.get("/")
async def root():
    return {"message": "Welcome to the Titanic API, we are learning on codanics.com"}

# Define a route
@app.get("/survival_rate")
async def get_survival_rate():
    return survival_rate.to_dict(orient="records")
