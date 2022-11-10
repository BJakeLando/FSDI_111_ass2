from flask import Flask, request
from app.database import task

app = Flask(__name__)

@app.get("/tasks")
def get_all_tasks():
    out ={}
    response = task.scan()
    out["tasks"] = response
    return out


@app.post("/tasks")
def create_task():
    out = {"status": "ok"}
    task_data = request.json
    task.insert(task_data)
    return out, 201

@app.put("/tasks/<id>")
def update_task(id):

    task_data = request.json

    task.update(id, task_data)
    return '', 204


@app.delete("/tasks/<id>")
def delete_task(id):
    task.delete(id)
    return '', 204

