from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List
import json
from pathlib import Path

app = FastAPI(title="Task Tracker Service")

DATA_FILE = Path("tasks_storage.txt")


# ----------------------------
# Data Models
# ----------------------------

class TaskRecord(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool


class TaskInput(BaseModel):
    title: str
    description: Optional[str] = None


# ----------------------------
# File Handling Utilities
# ----------------------------

def read_storage() -> List[dict]:
    if not DATA_FILE.exists():
        return []

    with DATA_FILE.open("r", encoding="utf-8") as file:
        lines = file.readlines()

    return [json.loads(line.strip()) for line in lines if line.strip()]


def write_storage(tasks: List[dict]) -> None:
    with DATA_FILE.open("w", encoding="utf-8") as file:
        for task in tasks:
            file.write(json.dumps(task) + "\n")


def generate_next_id(tasks: List[dict]) -> int:
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


# ----------------------------
# API Endpoints
# ----------------------------

@app.get("/")
def service_status():
    return {"status": "Task Tracker Service is active"}


@app.get("/tasks")
def list_tasks(status: Optional[bool] = None):
    stored_tasks = read_storage()

    if status is None:
        return {"count": len(stored_tasks), "tasks": stored_tasks}

    filtered = [task for task in stored_tasks if task["completed"] == status]
    return {"count": len(filtered), "tasks": filtered}


@app.get("/tasks/{task_id}")
def retrieve_task(task_id: int):
    stored_tasks = read_storage()

    for task in stored_tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Requested task does not exist.")


@app.get("/tasks-overview")
def summarize_tasks():
    stored_tasks = read_storage()

    total = len(stored_tasks)
    completed = sum(1 for task in stored_tasks if task["completed"])
    pending = total - completed
    percentage = round((completed / total) * 100, 2) if total else 0

    return {
        "total_tasks": total,
        "completed_tasks": completed,
        "pending_tasks": pending,
        "completion_rate_percent": percentage
    }


@app.post("/tasks", status_code=201)
def create_task(payload: TaskInput):
    stored_tasks = read_storage()

    new_task = TaskRecord(
        id=generate_next_id(stored_tasks),
        title=payload.title,
        description=payload.description,
        completed=False
    )

    stored_tasks.append(new_task.dict())
    write_storage(stored_tasks)

    return new_task


@app.put("/tasks/{task_id}")
def modify_task(task_id: int, payload: TaskInput):
    stored_tasks = read_storage()
    updated = False

    for index, task in enumerate(stored_tasks):
        if task["id"] == task_id:
            stored_tasks[index] = {
                "id": task_id,
                "title": payload.title,
                "description": payload.description,
                "completed": task["completed"]
            }
            updated = True
            break

    if not updated:
        raise HTTPException(status_code=404, detail="Task ID not found.")

    write_storage(stored_tasks)
    return {"message": "Task successfully updated.", "task": stored_tasks[index]}


@app.patch("/tasks/{task_id}/toggle")
def toggle_completion(task_id: int):
    stored_tasks = read_storage()

    for task in stored_tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            write_storage(stored_tasks)
            return {"message": "Completion status toggled.", "task": task}

    raise HTTPException(status_code=404, detail="Task not found.")


@app.delete("/tasks/{task_id}")
def remove_task(task_id: int):
    stored_tasks = read_storage()
    new_list = [task for task in stored_tasks if task["id"] != task_id]

    if len(new_list) == len(stored_tasks):
        raise HTTPException(status_code=404, detail="Task not found.")

    write_storage(new_list)
    return {"message": "Task deleted successfully.", "remaining_tasks": new_list}


@app.delete("/tasks")
def clear_all_tasks():
    write_storage([])
    return {"message": "All tasks have been removed."}
