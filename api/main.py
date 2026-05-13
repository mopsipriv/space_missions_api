from fastapi import FastAPI

app = FastAPI(title="Space Missions API",description="Space Missions", version="1.0.0")

@app.get("/")
def hello():
    return{"message": "Welcome Space Missions API","docs_url": "/docs"}

