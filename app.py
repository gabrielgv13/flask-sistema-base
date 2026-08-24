import json
import os

from flask import Flask, jsonify, render_template, request

DATA_FILE = "data.json"
app = Flask(__name__)


def read_users():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def write_users(users):
    with open(DATA_FILE, "w") as f:
        json.dump(users, f)


def add_user(user):
    users = read_users()
    users.append(user)
    write_users(users)


# --- Web interface ---

@app.route("/")
def index():
    return render_template("index.html", users=read_users())


@app.route("/add", methods=["POST"])
def add_user_web():
    email = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()
    if email and password:
        add_user({"email": email, "password": password})
    return render_template("index.html", users=read_users())


# --- API ---

@app.route("/api/users", methods=["GET"])
def api_get_users():
    return jsonify(read_users())


@app.route("/api/users", methods=["POST"])
def api_add_user():
    data = request.get_json(silent=True) or {}
    email = data.get("email", "").strip()
    password = data.get("password", "").strip()
    if not email or not password:
        return jsonify({"error": "email and password required"}), 400
    add_user({"email": email, "password": password})
    return jsonify({"ok": True}), 201


if __name__ == "__main__":
    app.run(debug=True)
    if not os.path.exists(DATA_FILE):
        write_users([])
