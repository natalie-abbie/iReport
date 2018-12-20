from flask import Blueprint,Flask, jsonify, json, request

user = Blueprint('users', __name__)

users_list = []
loggedinuser = []

# routes for the api

@user.route('/api/v1/register', methods=['POST'])
def register():
    data = request.get_json()

    firstname = data['firstname']
    secondname = data['secondname']
    username = data['username']
    email = data['email']
    password = data['password']

    try:
        firstname = data['firstname']
        secondname = data['secondname']
        username = data['username']
        email = data['email']
        password = data['password']

    except KeyError as item:
        return jsonify({'message': str(item)+'missing'}), 400

    users = {
        'firstname': firstname,
        'secondname': secondname,
        'username': username,
        'email': email,
        'password': password
    }
    users_list.append(users)

    for users in users_list:
        if not len(firstname) > 0 and not len(secondname) >0 and not len(username) > 0 :
            return jsonify({"message": "field can't be blank"}), 400 
        
        if not len(email) > 0 and not len(password) > 0:
            return jsonify({"message": "field can't be blank"}), 400
        
        else:
            return jsonify({"message": "Account created successfully", 'users': users_list}), 200

# Login
@user.route('/api/v1/login', methods=['POST'])
def login():

    data = request.get_json()

    username = data['username']
    password = data['password']
    role = data['role']

    try:
        username = data['username']
        password = data['password']
        role = data['role']

    except KeyError as item:
        return jsonify({'message': str(item)+'missing'}), 400

    users = {
        'username': username,
        'password': password,
    }

    for users in users_list:

        if not len(username) > 0 and not len(password) > 0:
            return jsonify({"message": "field can't be blank"}), 400 

        if username == username and password == password:
            return jsonify({"message": "login successful"}), 200
        
        if username != username and password != password:
            return jsonify({"message": "invalid"}), 400

        else:
           return jsonify({"message":"invalid"}), 400
            


@user.route('/api/v1/session', methods=['POST'])
def session():

    username = []
    optiondata = request.get_json()

    option = optiondata["your option"]
    if option == "logout":
        return jsonify({"message": "you are logged out"}), 200


@user.route('/api/v1/order', methods=['GET'])
def get_order():
    if len(users_list) == 0:
        return jsonify({"message":"no registered user"})
    return jsonify({'users': users_list}), 200