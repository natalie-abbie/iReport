from flask import Flask, Blueprint, jsonify, json, request
from datetime import datetime 
from functools import wraps
from main.models.model import FLAGS, Redflag
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from  main.views.users import loggedinuser

flags = Blueprint('flag',__name__)

redflag_list = []

@flags.route("/api/v1/create_redflag", methods=['POST'])
def create_redflag():
    
    try:
        if request.content_type != 'application/json':
            return jsonify({'Bad request': 'Content-type must be in json'}), 400
            
        request_data = request.get_json()

        if not request_data:
            return jsonify({"Failed": "Request can't be empty"}), 400

        global loggedinuser
        global FLAGS

        if len(loggedinuser) == 0:
            return jsonify({'message':'please login to create a flag'}), 401 # unauthorized access
    
        if 'type' not in request_data.keys():
            return jsonify({'message':'Flag type is missing'}), 400 #bad request

        if 'location' not in request_data.keys():
            return jsonify({'message':'location is missing'}), 400 #bad request

        if 'description' not in request_data.keys():
            return jsonify({'message':'description is missing'}), 400 #bad request

        if 'createdby' not in request_data.keys():
            return jsonify({'message':'createdby is missing'}), 400 #bad request

        if 'createdOn' not in request_data.keys():
            return jsonify({'message':'createdby is missing'}), 400 #bad request

        if len(request_data['description']) < 20:
            return jsonify({'message':'description should be well defined'}), 400 #bad request

         #create class object for redflag class 
        flags2 = Redflag(str(uuid4()), request_data['type'], loggedinuser[0], request_data['location'], request_data['description'], request_data['createdby'],request_data['createdOn'])


         # parameters [{flag_id:[type,user_id,description,email,location,createdOn,createdby]}]
        result = flags2.create_redflag()
        
        if result:
            return jsonify({'message': 'flag successfully created'}), 201 #created
        
        return jsonify({'message':'flag was not created, try again'}), 400 #conflict


        type = request_data['type']
        location = request_data['location']
        description = request_data['description']
        createdOn = request_data['createdOn']
        createdby = request_data['createdby']
        
      

    except KeyError as item:
       return jsonify({'message': str(item) + 'missing'}), 400

# only viewed by admin through the admin accesselse:
                
@flags.route('/api/v1/redflag', methods=['GET'])
def get():
    """"Function that returns all registered flags"""
    global FLAGS
    if not FLAGS:
        return jsonify({'message':'No records found'}), 404 #not found
    else:        
        return jsonify({'flags': FLAGS}), 200

@flags.route('/api/v1/redflag/<flag_id>', methods=['GET'])
def get_specific_flag(flag_id):
    """ function to retrieve a single flag by id"""
    global FLAGS    

    if not FLAGS:
        return jsonify({'message':'no records of any flag exist.'}), 404 #not found
    else:
        result = Redflag.get_specific_flag(id)
        if result or result == 0:
            return jsonify({'flag':FLAGS[result]}), 200 #ok
        else:
            return jsonify({'business':'no records of that business exist'}), 400 #bad request
    
@flags.route("/api/v1/redflag/<flag_id>/update", methods=['PATCH'])
def update(flag_id):
    """Function to update flag using the id passed from parameter"""
    global FLAGS
    global loggedinuser

    if len(loggedinuser) == 0:
        return jsonify({'message':'you are logged out, please login'}), 401 #anauthorized access

    if FLAGS:

        request_data = request.get_json()
        
        exists = Redflag.get_specific_flag(id)
        flag_id = ''
        
        if len(request_data.keys()) != 4:
            return jsonify({'message':'some fields are missing, try again'}), 400 #bad request

        if request_data['type']:
            type = request_data['type']
        else:
            type = ''

        if request_data['location']:
            location = request_data['location']
        else:
            location = ''

        if request_data['media']:
            media = request_data['media']
        else:
            media = ''
        
        if request_data['description']:
            description = request_data['description']
        else:
            description = ''
        
        if exists or exists == 0:
            result = FLAGS[exists]
            for k in result.items():
                flag_id = k
                FLAGS[exists] = {flag_id : [type, loggedinuser[0],description,location, media]}
                return jsonify({'message':'flag has been updated successfully'}), 200 #ok
        else:
            return jsonify({'message': 'no records of that flag exist'}), 404 #not found

        
@flags.route("/api/v1/redflag/<flag_id>/description", methods=['PATCH'])
def update1(flag_id):
    """Function to update flag description using the id passed from parameter"""
    global FLAGS
    global loggedinuser

    if len(loggedinuser) == 0:
        return jsonify({'message':'you are logged out, please login'}), 401 #anauthorized access

    if FLAGS:

        request_data = request.get_json()
        
        exists = Redflag.get_specific_flag(id)
        flag_id = ''
        
        if len(request_data.keys()) != 4:
            return jsonify({'message':'some fields are missing, try again'}), 400 #bad request

        if request_data['description']:
            description = request_data['description']
        else:
            description = ''

        if exists or exists == 0:
            result = FLAGS[exists]
            for k in result.items():
                flag_id = k
                FLAGS[exists] = {flag_id : [loggedinuser[0],description]}
                return jsonify({'message':'flag description has been updated successfully'}), 200 #ok
        else:
            return jsonify({'message': 'no records of that flag exist'}), 404 #not found


@flags.route("/api/v1/redflag/<flag_id>", methods=['DELETE'])
def delete_flag(id):
    """Function is responsible for deleting a flag on parameter passed as id"""
    global FLAGS    
    
    if FLAGS:
        result = Redflag.delete_flag(id)
        # print(result)
        if result or result == 0:
            FLAGS.pop(result)
            return jsonify({'message':'flag has been successfully deleted'}), 200 #ok
        else:
            return jsonify({'message':'No flag has that id, nothing was deleted'}), 400 #bad request
    else:
        return jsonify({'message': 'no records of any flag exist'}), 404 #not found