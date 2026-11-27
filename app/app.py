
from flask import Flask, render_template_string, request, redirect
import sqlite3
import os

app = Flask(__name__)

DATABASE = os.getenv("DATABASE_PATH", "/app/database/tasks.db")

def init_db():
    os.makedirs(os.path.dirname(DATABASE), exist_ok=True)

    conn = sqlite3.connect(DATABASE)
    conn.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Cloud Task Manager</title>
    <style>
        body {
            font-family: Arial;
            background: #eef2ff;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: white;
            padding: 30px;
            max-width: 500px;
            margin: auto;
            border-radius: 15px;
        }
        input {
            padding: 12px;
            width: 65%;
        }
        button {
            padding: 12px;
            background: #4f46e5;
            color: white;
            border: none;
            cursor: pointer;
        }
        li {
            padding: 10px;
            text-align: left;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>☁️ Cloud Task Manager</h1>
        <p>My Cloud Deployment Project</p>

        <form method="POST">
            <input name="task" placeholder="Enter a task" required>
            <button type="submit">Add Task</button>
        </form>

        <h3>My Tasks</h3>
        <ul>
            {% for task in tasks %}
                <li>{{ task[1] }}</li>
            {% endfor %}
        </ul>
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task", "").strip()

        if task:
            conn = sqlite3.connect(DATABASE)
            conn.execute(
                "INSERT INTO tasks (task) VALUES (?)",
                (task,)
            )
            conn.commit()
            conn.close()

        return redirect("/")

    conn = sqlite3.connect(DATABASE)
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()

    return render_template_string(HTML, tasks=tasks)

@app.route("/health")
def health():
    return {"status": "healthy"}

init_db()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
