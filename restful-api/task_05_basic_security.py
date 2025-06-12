#!/usr/bin/python3
from functools import wraps
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (create_access_token, verify_jwt_in_request, 
                                jwt_required, JWTManager, get_jwt_identity)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "keep-it-secret-keep-it-safe"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
        },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"}
}

@auth.verify_password
def is_user(username, password):
    if (username in users and 
            check_password_hash(users[username]["password"], password)):
        return username
    return None

# def admin_required():
#     def wrapper(fn):
#         @wraps(fn)
#         def decorator(*args, **kwargs):
#             verify_jwt_in_request()
#             claims = get_jwt()
#             if claims["is_admin"]:
#                 return fn(*args, **kwargs)
#             else:
#                 return jsonify(msg={{"error": "Admin access required"}}), 403
#         return decorator
#     return wrapper

@app.route('/')
def home():
    return "welcome home", 200


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted", 200


@app.route('/login', methods=['POST'])
def login():
    data = request.json()
    username = data.get('username')
    password = data.get('password')
    if (username not in users or 
            check_password_hash(users[username]["password"], password)):
        return "401 Unauthorized", 401

    access_token = create_access_token(
        identity={"username": username, "role": users[username]['role']}
        )
    return jsonify(access_token=access_token)


@app.route('/jwt-protected')
@jwt_required()
def protected_route():
    return "JWT Auth: Access Granted", 200


@app.route('/admin-only')
@jwt_required
def admin_page():
    current_user = get_jwt_identity()
    if current_user["role"] == "admin":
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Admin access required"}), 403

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return "401 Unauthorized", 401

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return "error: Missing or invalid token", 401


if __name__ == "__main__":
    app.run()