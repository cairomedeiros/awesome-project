from fastapi import FastAPI
from app.routers import todo

app = FastAPI()

app.include_router(todo.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}