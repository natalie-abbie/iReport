from flask import Blueprint, Flask, jsonify, json, request
import re
import datetime 


user = Blueprint('users', __name__)

users_list = []
loggedinuser = []

# routes for the api

@user.route('/api/v1/register', methods=['POST'])
def register():
    """
    User creates an account
    User sign up details are added to the data base
    """

    try:
        if request.content_type != 'application/json':
            return jsonify({'Bad request':'Content-type must be json type'}), 400

        request_data = request.get_json()

        if not request_data:
            return jsonify({"message": "Request not made"}), 400

        user_id = request_data['user_id']
        firstname = request_data['firstname']
        lastname = request_data['lastname']
        othernames = request_data['othername']
        phonenumber = request_data['phonenumber']
        email = request_data['email']
        username =  request_data['username']
        password = request_data['password']
        isAdmin = request_data['isAdmin']
        registeredon = datetime.datetime.now()
        
        users = {
            'user_id': user_id,
            'firstname': firstname,
            'lastname': lastname,
            'othername': othernames,
            'username': username,
            'phonenumber': phonenumber,
            'password': password,
            'email': email,
            'isAdmin': isAdmin,
            'datetime.datetime.now()': registeredon   
        }

        users_list.append(users)

        for users in users_list:

            if len(firstname) and len(lastname) and len(othernames) < 3:
                return jsonify({'Missing': 'Name is required'}), 400

            if len(phonenumber) < 10:
                return jsonify({'Invalid': 'phone number should be atleast 10 characters'}), 400

            if not re.match("[0-9]", phonenumber):
                return jsonify({'Invalid': 'phone number should only contain numbers'}), 400

            # if not isinstance(username, str):
            #     return jsonify({'Invalid': 'username should be of type string'}), 400

            if len(username) < 3:
                return jsonify({'Invalid': 'username should be atleast 3 characters'}), 400

            if len(username) < 0:
                return jsonify({'Missing':'Username required'}), 400

            if not email:
                return jsonify({'Error':'Missing or wrong email format'}), 400

            if not len(request_data['password']) > 5:
                return jsonify({'Failed': 'password must be atleast 6-8 characters'}), 400
        
        else:
            return jsonify({"message": "Account created successfully", 'users': users_list}), 200

    except KeyError as item:
        return jsonify({'Error': str(item) + ' is missing'}), 400


# user Login
@user.route('/api/v1/login', methods=['POST'])
def login():
    """
    User login with correct credentials
    token is generated and given to a user
    """

    try:

        if request.content_type != 'application/json':
            return jsonify({'Bad request': 'Content-type must be in json'}), 400
            
        request_data = request.get_json()

        if not request_data:
            return jsonify({"Failed": "Request can't be empty"}), 400

        email = request_data['email']
        password = request_data['password']


        users = {
            'email': email,
            'password': password,
        }

        loggedinuser.append(users)

        for users in users_list:

            if request_data['email'] != email and request_data['password'] != password:
                return jsonify({'Failed': 'email or password is invalid'}), 400
            
            if request_data['email'] < 0 and request_data['password'] < 0:
                return jsonify({'Failed': 'field cant be empty'}), 400

            if email == email and password == password:
                return jsonify({"message": "login successful"}), 200
        else:
            return jsonify({'message':'invalid'}), 400
            
    except KeyError as item:
        return jsonify({'message': str(item)+'missing'}), 400

    #     payload = {
    #         'exp': datetime.datetime.utcnow() +
    #                datetime.timedelta(days=0, hours=23),
    #         'user_id': user_id,
    #         'email': email,
    #         'isAdmin': new_user.isAdmin
    #     }

    #     token = jwt.encode(
    #         payload,
    #         'talieatalia',
    #         algorithm='HS256'
    #     )

    #     if token:
    #         return jsonify({"message": "logged in successfully ", "auth_token": token.decode('UTF-8'),'user_id':new_user.user_id,'isADmin':new_user.isADmin}), 200

    # except:
    #        pass


# @user.route('/api/v1/session', methods=['POST'])
# def session():

#     othernames = []
#     optiondata = request.get_json()

#     option = optiondata["your option"]
#     if option == "logout":
#         return jsonify({"message": "you are logged out"}), 200


# @user.route('/api/v1/order', methods=['GET'])
# def get_order():
#     if len(users_list) == 0:
#         return jsonify({"message":"no registered user"})
#     return jsonify({'users': users_list}), 200