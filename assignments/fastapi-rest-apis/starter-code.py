from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI(title="FastAPI - ToDo Demo")


class TaskIn(BaseModel):
    title: str


class Task(TaskIn):
    id: int


# In-memory storage
tasks: List[Task] = []
next_id = 1


@app.get("/tasks", response_model=List[Task])
def list_tasks():
    return tasks


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for t in tasks:
        if t.id == task_id:
            return t
    raise HTTPException(status_code=404, detail="Task not found")


@app.post("/tasks", response_model=Task, status_code=201)
def create_task(payload: TaskIn):
    global next_id
    task = Task(id=next_id, title=payload.title)
    tasks.append(task)
    next_id += 1
    return task


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("starter-code:app", host="127.0.0.1", port=8000, reload=True)
