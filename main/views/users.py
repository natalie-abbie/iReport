from flask import Blueprint, Flask, jsonify, json, request, make_response
import re
import datetime 
from main.models.model import User, USERS
import jwt
from uuid import uuid4
from functools import wraps
from werkzeug.security import generate_password_hash, check_password_hash


user = Blueprint('users', __name__)

SECRETKEY = 'TaLiEatalie'
token = None


loggedinuser = []

# routes for the api

@user.route('/api/v1/auth/register', methods=['POST'])
def register():
    """
    User creates an account
    User sign up details are added to the request_data base
    """
    

    try:
        global USERS

        if request.content_type != 'application/json':
            return jsonify({'Bad request':'Content-type must be json type'}), 400

        request_data = request.get_json()

        if not request_data:
            return jsonify({"message": "Request not made"}), 400
       
        # validate username
        if 'username' not in request_data.keys():
            return jsonify({'message':'username is missing'}), 400 #bad request
        else:
            username = request_data['username'] 

        # valid phone number
        if 'phonenumber' not in request_data.keys():
            return jsonify({'Invalid': 'phone number should be atleast 10 characters'}), 400

        if not len(request_data['phonenumber']) < 10:
            return jsonify({'Failed': 'phonenumber must be 10 characters'}), 400
        
        if "[0-9]" not in request_data['phonenumber']:
                return jsonify({'Invalid': 'phone number should only contain numbers'}), 400
        else:
            phonenumber = request_data['phonenumber']

       
        #check that email is not missing
        if 'email' not in request_data.keys():
            return jsonify({'message':'email is missing'}), 400 #bad request
        else:
            email = request_data['email']

        #valid password
        if 'password' not in request_data.keys():
            return jsonify({'message':'password is missing'}), 400 #bad request
        
        if not len(request_data['password']) > 5:
            return jsonify({'Failed': 'password must be atleast 6-8 characters'}), 400
       
        else:
            password = request_data['password']

         #check whether username has already been taken.
        for x in USERS:
            for v in x.items():
                if v == username:            
                    return jsonify({'message':'user already exists'}), 400 #bad request
    
        password = generate_password_hash(password)            
        USERS.append({"userid":str(uuid4()), "username":username, "email":email, "password":password})
        return jsonify({"message":"Account created successfully"}), 201 #created

    except KeyError as item:
        return jsonify({'Error': str(item) + ' is missing'}), 400

@user.route('/api/v1/getuser', methods=['GET'])
def get_users():
    global USERS    
    if not USERS:
        return jsonify({'message':'No users found in the system'})
    else:
        usersx = USERS
        return jsonify({"USERS":usersx})

# user Login
@user.route('/api/v1/auth/login', methods=['POST'])
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

        global loggedinuser
        global USERS
        auth = request.authorization

        if not USERS:
            return jsonify({'message':'you are not yet registered'}), 401 # unauthorized access
    
        if auth:
            username = auth.username
            password = auth.password
            token = jwt.encode({'user':auth.username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRETKEY)
            
            if USERS:            
                for x in USERS:
                    for k in x:
                        if x['username'] == username and check_password_hash(x['password'], password):
                            loggedinuser.append([x['userid'], x['username']])                  
                            return jsonify({'token': token.decode('UTF-8'), 'message':'logged in successfully'}), 200
                            # return jsonify({'message':'Logged in Successfully'}), 200
                        else:                        
                            return jsonify({'message':'unauthorised access, invalid username or password'}), 400

        elif request_data:

            if 'username' not in request_data.keys():
                return jsonify({'message':'username is missing'}), 400

            if 'password' not in request_data.keys():
                return jsonify({'message':'password is missing'}), 400

            username = request_data['username']
            password = request_data['password']
            # token = jwt.encode({'user':username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRETKEY)

            # if loggedInUser[1] == username:
            #     return jsonify({'message':'you are already logged in'}), 400 #bad request
            
            if USERS:
                for x in USERS:
                    for k in x:
                        if x['username'] == username and check_password_hash(x['password'], password):
                            loggedinuser.append([x['userid'], x['username']])                  
                            # return jsonify({'token': token.decode('UTF-8'), 'message':'logged in successfully'}), 200
                            return jsonify({'message':'logged in successfully'}), 200
                        else:                        
                            return jsonify({'message':'unauthorised access, invalid username or password'}), 401 # bad request
        
        else:
            return jsonify({"message":"Could not verify authetication"}), 401  # unauthorised access
            
        return make_response(jsonify({'message':'couldn''t verify login'})), 401 # unauthorised access

    except KeyError as item:
        return jsonify({'Error': str(item) + ' is missing'}), 400


@user.route('/api/v1/auth/resetpassword', methods=['POST'])
def reset_password():
    global USERS
    global loggedinuser 

    request_data = request.get_json()

    if len(request_data.keys()) == 0:
        return jsonify({'message':'nothing has been provided'}), 400

    if 'password' not in request_data.keys():
        return jsonify({'message':'password field is missing'}), 400

    new_password = request_data['password']

    #check that we have users registered
    if not USERS:
        return jsonify({"message":"no users found, first register"}), 404 # not found

    #check if user is already logged in
    if len(loggedinuser) == 0:
        return jsonify({"message":"please first login"}), 401 # unauthorized access

    #get username for current logged in user    
    for x in loggedinuser:
        username = x[1]

    # lets only reset password for currently logged in user.
    for x in USERS:
        for k, v in x.items():
            if k == 'username':
                if v == username:
                    x['password'] = generate_password_hash(new_password)
                    return jsonify({'message':'password was reset successfully'}), 200
            
    return jsonify({'message':'password reset was not successful'}), 400

@user.route('/api/v1/auth/resetpassword', methods=['POST'])
def logout():
    global loggedinuser
    global USERS   

    if not loggedinuser:
        return jsonify({'message':'you are already logged out'}), 400 #bad request

    if len(loggedinuser) > 0:
        del loggedinuser[:]
        request.authorization = None
        return jsonify({'message':'you have successfully logged out'}), 200 #ok
    else:        
        return jsonify({'message':'something went wrong, please try again'}), 400 #bad request
    