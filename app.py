from fastapi import FastAPI, Path, Body
import uvicorn
from pydantic import BaseModel, Field

app = FastAPI(title="Sample FastAPI",
              description="For education", version="1.0")

@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
	uvicorn.run("app:app", port=5000, log_level="info", reload=True, host="0.0.0.0")