from flask import Flask, request

app = Flask(__name__)
app.json.sort_keys = False

users = {}

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
        return {"error": "User not found"}, 404
    return users[username]


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    if data is None:
        return {"error": "Username is required"}, 400
    required_keys = {"username", "name", "age", "city"}
    if not required_keys.issubset(data.keys()):
        return {"error": "Username is required"}, 400
 
    users[data["username"]] = data

    return {
        "message": "User added",
        "user": data
    }, 201

if __name__ == "__main__": 
    app.run()