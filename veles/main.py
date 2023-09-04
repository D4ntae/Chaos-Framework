from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def home_route():
    return "Hello World"
