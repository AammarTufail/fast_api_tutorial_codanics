from fastapi import FastAPI # for creating the FastAPI instance
from fastapi.responses import HTMLResponse # for returning HTML content
import seaborn as sns # for loading the Titanic dataset and plotting
import pandas as pd # for data manipulation
import matplotlib.pyplot as plt # for plotting
import base64 # for encoding the plot to base64 string (which is required for displaying the plot in HTML)
from io import BytesIO # for saving the plot to a BytesIO object

app = FastAPI()  # Create a FastAPI instance

# Load the Titanic dataset
df = sns.load_dataset('titanic')

# Perform a simple data transformation
survival_rate = df.groupby("class")["survived"].mean().reset_index()

@app.get("/")
async def root():
    return {"message": "Welcome to the Titanic API, we are learning on codanics.com"}

@app.get("/survival_rate")
async def get_survival_rate():
    return survival_rate.to_dict(orient="records")

@app.get("/survival_rate_plot", response_class=HTMLResponse)
async def survival_rate_plot():
    # Generate the plot
    sns.barplot(x="class", y="survived", hue="sex", data=df, capsize=0.05, errwidth=2, palette="viridis")
    plt.title('Survival Rate by Class')
    plt.ylabel('Survival Rate')
    plt.xlabel('Class')

    # Save the plot to a BytesIO object
    bytes_image = BytesIO()
    plt.savefig(bytes_image, format='PNG')
    plt.close()
    bytes_image.seek(0)

    # Encode the BytesIO object to base64 string
    base64_image = base64.b64encode(bytes_image.getvalue()).decode("utf-8")

    # Generate the HTML content
    html_content = f'<img src="data:image/png;base64,{base64_image}" alt="Survival Rate by Class">'
    return HTMLResponse(content=html_content)
