from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage for simplicity
data = {'users': ['abhishek','vishal','jahnavi']}

# GET method to retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(data)

# POST method to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    user = request.json
    data['users'].append(user)
    return jsonify(user), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
