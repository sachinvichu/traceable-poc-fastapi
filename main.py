from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Traceable POC"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello, {name}"}

@app.get("/status")
def status():
    return {"status": "running"}

# Ensure it runs on the correct port (dynamic $PORT from Railway)
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Railway injects $PORT
    uvicorn.run("main:app", host="0.0.0.0", port=port)

