from flask import Flask, Blueprint, jsonify, json, request

flags = Blueprint('flag',__name__)

redflag_list = []

@flags.route("/api/v1/create_redflag", methods=['POST'])
def post():
    global redflag_list

    userdata = request.get_json()
    try:
        location = userdata['location']
        type = userdata['type']
        description = userdata['description']
        media = userdata['media']

    except KeyError as item:
       return jsonify({'message': str(item) + 'missing'}), 400

    new_flag = {
       'location': location,
       'type': type,
       'description': description,
       'media': media
    }
    
    redflag_list.append(new_flag)

    for new_flag in redflag_list:
        if not len(location) > 0 and not len(type) >0:
            return jsonify({"message":"section cant be empty"}), 400
        
        if not len(description) > 0 and not len(media) >0:
            return jsonify({"message":"section cant be empty"}), 400
        
        else:
            return jsonify({"message": "redflag created"}), 201

@flags.route("/api/v1/update_flag", methods=['UPDATE', 'POST'])
def update(): 
    pass  

@flags.route("/api/v1/delete_flag", methods=['DELETE'])
def delete():
    pass

# only viewed by admin through the admin access
@flags.route('/api/v1/redflag', methods=['GET'])
def get():
    if len(redflag_list) == 0:
        return jsonify({"message":"No redflag posted"})
    return jsonify({'orders': redflag_list}), 200
