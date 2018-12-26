import uuid
from flask import Flask, Blueprint, jsonify, json, request
from datetime import datetime as dt

flags = Blueprint('flag',__name__)

redflag_list = []

@flags.route("/api/v1/create_redflag", methods=['POST'])
def post():
    
    userdata = request.get_json()
    try:
        flag_id =uuid.uuid1()
        location = userdata['location']
        type = userdata['type']
        description = userdata['description']
        image = userdata['image']
        video = userdata['video']
        created_on = dt.utcnow()
        created_by = userdata['created_by']

    except KeyError as item:
       return jsonify({'message': str(item) + 'missing'}), 400

    data = {
        'flag_id':uuid.uuid1(),
        'location': location,
        'type': type,
        'description': description,
        'image': image,
        'video' : video,
        str(dt.utcnow()) : created_on,
        'created_by' : created_by
    }
    
    redflag_list.append(data)

    for data in redflag_list:
        if not len(location) > 0 and not len(type) >0:
            return jsonify({"message":"section cant be empty"}), 400
        
        if not len(description):
            return jsonify({"message":"section cant be empty"}), 400
        
        else:
            return jsonify("'status': 201",{'data': redflag_list,"id":flag_id, 'message': "redflag created"}), 201

# only viewed by admin through the admin access
@flags.route('/api/v1/redflag', methods=['GET'])
def get():
    if len(redflag_list) == 0:
        return jsonify({"message":"No redflag posted"})
    return jsonify({
                    'status': 201,
                    'data': redflag_list}), 200

@flags.route('/api/v1/redflag/<flag_id>', methods=['GET'])
def get1(flag_id):
    for flag_id in redflag_list:
        if flag_id == flag_id:
            return jsonify({
                    'data': redflag_list}), 200
        else:
            return jsonify({"message":"No redflag posted"})

@flags.route("/api/v1/redflag/<flag_id>/location", methods=['PATCH'])
def update(flag_id):
    for data in redflag_list:
        if flag_id == flag_id:
            data['location'] = request.get_json()
            return jsonify({"message":"redflag updated"})

@flags.route("/api/v1/redflag/<flag_id>/description", methods=['PATCH'])
def update1(flag_id):
    for data in redflag_list:
        if flag_id == flag_id:
            data['description'] = request.get_json()
            return jsonify({"message":"description updated"})


@flags.route("/api/v1/redflag/<flag_id>", methods=['DELETE'])
def delete(flag_id):
    for data in redflag_list:
        if flag_id == flag_id:
            redflag_list.remove(data)
            return jsonify({"message":"redflag deleted"})
