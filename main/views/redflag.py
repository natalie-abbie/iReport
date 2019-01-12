from flask import Flask, Blueprint, jsonify, json, request
from datetime import datetime
from functools import wraps
from models.model import FLAGS, Redflag
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from views.users import loggedinuser

flags = Blueprint('flag', __name__)

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
            # unauthorized access
            return jsonify({'message': 'please login to create a flag'}), 401

        if 'type' not in request_data.keys():
            # bad request
            return jsonify({'message': 'Flag type is missing'}), 400
        else:
            type = request_data['type']

        if 'location' not in request_data.keys():
            # bad request
            return jsonify({'message': 'location is missing'}), 400
        else:
            location = request_data['location']

        if 'description' not in request_data.keys():
            # bad request
            return jsonify({'message': 'description is missing'}), 400

        if 'createdby' not in request_data.keys():
            # bad request
            return jsonify({'message': 'createdby is missing'}), 400

        if 'createdOn' not in request_data.keys():
            # bad request
            return jsonify({'message': 'createdOn is missing'}), 400

        if len(request_data['description']) < 20:
            # bad request
            return jsonify({'message': 'description should be well defined'}), 400

         # create class object for redflag class
        flags2 = Redflag(str(uuid4()),loggedinuser[0],request_data['type'], request_data['location'],request_data['description'], request_data['createdby'])

        # parameters [{flag_id:[type,user_id,description,email,location,createdOn,createdby]}]
        result = flags2.create_redflag()

        if result:
            # created
            return jsonify({'message': 'flag successfully created', 'flags':FLAGS}), 201

        # conflict
        return jsonify({'message': 'flag was not created, try again'}), 400

        # type = request_data['type']
        # location = request_data['location']
        description = request_data['description']
        createdOn= request_data['createdOn']
        createdby = request_data['createdby']

    except KeyError as item:
        return jsonify({'message': str(item) + 'missing'}), 400

# only viewed by admin through the admin accesselse:


@flags.route('/api/v1/redflag', methods=['GET'])
def get():
    """"Function that returns all registered flags"""
    global FLAGS
    if not FLAGS:
        return jsonify({'message': 'No records found'}), 404  # not found
    else:
        return jsonify({'flags': FLAGS}), 200


@flags.route('/api/v1/redflag/<flag_id>', methods=['GET'])
def get_specific_flag(flag_id):
    """ function to retrieve a single flag by id"""
    global FLAGS

    if not FLAGS:
        # not found
        return jsonify({'message': 'no records of any flag exist.'}), 404
    else:
        result = Redflag.get_specific_flag(id)
        if result or result == 0:
            return jsonify({'flag': FLAGS[result]}), 200  # ok
        else:
            # bad request
            return jsonify({'flag': 'no records of that flag exist'}), 400


@flags.route("/api/v1/redflag/<flag_id>/update", methods=['PATCH'])
def update(flag_id):
    """Function to update flag using the id passed from parameter"""
    global FLAGS
    global loggedinuser

    if len(loggedinuser) == 0:
        # anauthorized access
        return jsonify({'message': 'you are logged out, please login'}), 401

    if FLAGS:

        request_data = request.get_json()

        exists = Redflag.get_specific_flag(id)
        flag_id = ''

        if len(request_data.keys()) != 4:
            # bad request
            return jsonify({'message': 'some fields are missing, try again'}), 400

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
                FLAGS[exists] = {
                    flag_id: [type, loggedinuser[0], description, location, media]}
                # ok
                return jsonify({'message': 'flag has been updated successfully'}), 200
        else:
            # not found
            return jsonify({'message': 'no records of that flag exist'}), 404


@flags.route("/api/v1/redflag/<flag_id>/description", methods=['PATCH'])
def update1(flag_id):
    """Function to update flag description using the id passed from parameter"""
    global FLAGS
    global loggedinuser

    if len(loggedinuser) == 0:
        # anauthorized access
        return jsonify({'message': 'you are logged out, please login'}), 401

    if FLAGS:

        request_data = request.get_json()

        exists = Redflag.get_specific_flag(id)
        flag_id = ''

        if len(request_data.keys()) != 4:
            # bad request
            return jsonify({'message': 'some fields are missing, try again'}), 400

        if request_data['description']:
            description = request_data['description']
        else:
            description = ''

        if exists or exists == 0:
            result = FLAGS[exists]
            for k in result.items():
                flag_id = k
                FLAGS[exists] = {flag_id: [loggedinuser[0], description]}
                # ok
                return jsonify({'message': 'flag description has been updated successfully'}), 200
        else:
            # not found
            return jsonify({'message': 'no records of that flag exist'}), 404


@flags.route("/api/v1/redflag/<flag_id>", methods=['DELETE'])
def delete_flag(id):
    """Function is responsible for deleting a flag on parameter passed as id"""
    global FLAGS

    if FLAGS:
        result = Redflag.delete_flag(id)
        # print(result)
        if result or result == 0:
            FLAGS.pop(result)
            # ok
            return jsonify({'message': 'flag has been successfully deleted'}), 200
        else:
            # bad request
            return jsonify({'message': 'No flag has that id, nothing was deleted'}), 400
    else:
        # not found
        return jsonify({'message': 'no records of any flag exist'}), 404
