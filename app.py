from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = []
next_id = 1

@app.get("/")
def home():
    return jsonify({
        "message": "To-Do List API is running",
        "endpoints": {"GET /tasks": "List tasks", "POST /tasks": "Create a task with JSON title"}
    })

@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.get("/tasks")
def get_tasks():
    return jsonify(tasks), 200

@app.post("/tasks")
def create_task():
    global next_id
    data = request.get_json(silent=True) or {}
    title = data.get("title", "")
    if not isinstance(title, str) or not title.strip():
        return jsonify({"error": "title is required"}), 400
    task = {"id": next_id, "title": title.strip(), "completed": False}
    next_id += 1
    tasks.append(task)
    return jsonify(task), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
