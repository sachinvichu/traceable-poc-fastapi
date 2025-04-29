# main.py

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, Welcome to Traceable POC!"}

@app.get("/status")
async def status():
    return {"status": "running fine"}

@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello, {name}!"}
# For Railway dynamic port support
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Use $PORT if available, else fallback to 8000
    uvicorn.run("main:app", host="0.0.0.0", port=port)
