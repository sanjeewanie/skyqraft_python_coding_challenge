from flask import jsonify, render_template, request, Blueprint
from src import mysql
from src.models import get_groups, get_group_all_details_by_name, insert_group, update_group_by_name, delete_group_by_name

groups = Blueprint('group_group', __name__,url_prefix='/group')

# ex: GET http://127.0.0.1:5000/group
@groups.route("/", methods=['GET'])
def list_groups():
    # get the list of all groups from db and return json
    groups = get_groups();
    return jsonify(groups)
    

# ex: POST http://127.0.0.1:5000/group
#{
# "name":"testgroup1"
# }
@groups.route("/", methods=['POST'])
def create_group():
    data=request.get_json(force=True)
    # save group to db
    resp=insert_group(data)
    return jsonify(resp)


# ex: GET http://127.0.0.1:5000/group/test
@groups.route("/<string:name>", methods=['GET'])
def get_group(name):
    # get the details of the group by 'name' from db and return it as json
    group = get_group_all_details_by_name(name)
    return jsonify(group)

# ex: POST http://127.0.0.1:5000/group/test
@groups.route("/<string:name>", methods=['POST'])
def update_group(name):
    data=request.get_json(force=True)
    # update the details of the group by 'name' with data and return it as json
    update_group_by_name(name, data)
    return jsonify("group Updated")

# ex: DELETE http://127.0.0.1:5000/group/test
@groups.route("/<string:name>", methods=['DELETE'])
def delete_group(name):
    # delete group by 'name'
    delete_group_by_name(name)
    return jsonify("group Deleted")