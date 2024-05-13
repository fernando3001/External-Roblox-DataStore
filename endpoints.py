from flask import Flask, jsonify, request
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "" # Your Mongo DB Url 

client = MongoClient(uri, server_api=ServerApi('1'))

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

app = Flask(__name__)

@app.route('/')
def route():
    return 'root'

@app.route('/users/', methods=['POST'])
def post_user():
    data = request.get_json()
    user_id = data.get('user_id')

    users_collection = client.mydatabase.users

    existing_user = users_collection.find_one({'user_id': user_id})
    if existing_user:
        return jsonify({"error": "User already exists"}), 400

    result = users_collection.insert_one(data)

    if result.acknowledged:
        return jsonify({"message": "User added successfully", "inserted_id": str(result.inserted_id)}), 201
    else:
        return jsonify({"error": "Failed to add user"}), 500

@app.route('/users/', methods=['GET'])
def get_users():
    user_id = request.args.get('user_id')

    if user_id:
        users_collection = client.mydatabase.users

        user = users_collection.find_one({"user_id": int(user_id)})

        if user:
            user['_id'] = str(user['_id'])
            return jsonify(user), 200
        else:
            return jsonify({"error": "User not found"}), 404
    else:
        return jsonify({"error": "Please provide user_id in the URL"}), 400

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):

    data = request.get_json()

    users_collection = client.mydatabase.users

    result = users_collection.update_one({"user_id": int(user_id)}, {"$set": data})

    if result.modified_count > 0:
        return jsonify({"message": "User updated successfully"}), 200
    else:
        return jsonify({"error": "User not found or no changes made"}), 404

if __name__ == '__main__':
    app.run(debug=True)
