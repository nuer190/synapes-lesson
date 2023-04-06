from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Sample FastAPI",
              description="For education", version="1.0")

data = {1:"john", 2: "jame"}
@app.get("/api/people")
def read_root():
    return data

@app.get("/api/people")
def read_root():
    return data[id]


if __name__ == "__main__":
    uvicorn.run("app:app", port=5000, log_level="info", reload=True, host="0.0.0.0")