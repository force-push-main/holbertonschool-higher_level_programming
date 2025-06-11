from flask import Flask, jsonify, request

app = Flask(__name__)

users = {"alice": {
        "username": "alice",
        "name": "Alice",
        "age": 25,
        "city": "San Francisco"
}}

@app.route('/')
def home():
    return "Welcome to the Flask API!"


@app.route('/data')
def get_data():
    return [username for username in users]


@app.route('/status')
def api_status():
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    if username not in users:
        return {"error": "User not found"}
    return users[username]


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.data
    if data is None:
        return {"error": "Username is required"}
    return data

if __name__ == "__main__": 
    app.run()