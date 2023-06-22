from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
async def root():
    app_name = os.getenv("APP_NAME", "root")
    
    return {
        "app_name": app_name,
        "message": "Hello, Pacmann Student!"
    }