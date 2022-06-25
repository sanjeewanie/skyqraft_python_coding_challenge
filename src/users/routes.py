from flask import jsonify, render_template, request, Blueprint
from src import mysql
from src.models import get_users, get_user_by_name,get_user_all_details_by_name, insert_user, update_user_by_name, deleter_user_by_name

users = Blueprint('users', __name__,url_prefix='/user')

# ex: GET http://127.0.0.1:5000/user
@users.route("/", methods=['GET'])
def list_users():
    # get the list of all users from db and return json
    users = get_users();
    return jsonify(users)
    

# ex: POST http://127.0.0.1:5000/user     Add the user elon
# {
# "name":"elon",
# "email":"test@gmail.com",
# "status":"1",
# "title":"Mrs"  
# }
#
@users.route("/", methods=['POST'])
def create_user():
    data=request.get_json(force=True)
    # save user to db
    resp=insert_user(data)
    return jsonify(resp)

# ex: GET http://127.0.0.1:5000/user/elon
@users.route("/<string:name>", methods=['GET'])
def get_user(name):
    # get the details of the user by 'name' from db and return it as json
    #user = get_user_by_name(name)
    user = get_user_all_details_by_name(name)
    
    return jsonify(user)

# ex: POST http://127.0.0.1:5000/user/elon
# {
# "name":"new_elon",
# "email":"new_test@gmail.com",
# "status":"0",
# "title":"Miss"  
# }
@users.route("/<string:name>", methods=['POST'])
def update_user(name):
    data=request.get_json(force=True)
    # update the details of the user by 'name' with data and return it as json
    resp=update_user_by_name(name, data)
    return jsonify(resp)

# ex: DELETE http://127.0.0.1:5000/user/elon
@users.route("/<string:name>", methods=['DELETE'])
def delete_user(name):
    # delete user by 'name'
    resp=deleter_user_by_name(name)
    return jsonify(resp)