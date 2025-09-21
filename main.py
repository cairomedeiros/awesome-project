from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

class Todo(BaseModel):
    id: int
    title: str
    description: str | None
    completed: bool = False

todos = []

@app.post("/todos/")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "created", "todo": todo}

@app.get("/todos/")
def get_todos():
    return {"message": "todo list", "todos": todos}

@app.get("/todos/{todo_id}")
def get_todos(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"message": "found", "todo": todo}
        
@app.put("/todos/{todo_id}")
def update_todos(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return {"message": "updated", "todo": updated_todo}
    return {"message": "todo item not found", "todo id": todo_id}

@app.delete("/todos/{todo_id}")
def update_todos(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(index)
            return {"message": "deleted"}
    return {"message": "todo item not found", "todo id": todo_id}