from flask import jsonify, render_template, request, Blueprint
from src import mysql
from src.models import get_all_assignments ,insert_user_assignments ,insert_group_assignments ,insert_project_assignments

main = Blueprint('main', __name__,url_prefix='/assign')

# ex: GET http://127.0.0.1:5000/assign
@main.route("/", methods=['GET'])
def list_all_assignments():
    # get the list of all users assignments from db and return json
    assignments = get_all_assignments()
    return jsonify(assignments)




# ex: POST http://127.0.0.1:5000/assign/user
# {
# "name":"elon",
# "project":"model3",
# "role":"owner" 
# }
# 
@main.route("/user", methods=['POST'])
def set_user_assignments():
    # save user assignments to db
    data=request.get_json(force=True)
    print(data)
    resp=insert_user_assignments(data)
    return jsonify(resp)



# ex: POST http://127.0.0.1:5000/assign/group
# { 
# "name":"tesla",
# "user":"elon"
# }
@main.route("/group", methods=['POST'])
def set_group_assignments():
    # get the list of all group assignments from db and return json
    data=request.get_json(force=True)
    resp=insert_group_assignments(data)
    return jsonify(resp)   


# ex: POST http://127.0.0.1:5000/assign/project
# {   
# "name":"model3",
# "group":"tesla",
# "role":"owner" 
# }
@main.route("/project", methods=['POST'])
def set_project_assignments():
    # get the list of all group assignments from db and return json
    data=request.get_json(force=True)
    resp=insert_project_assignments(data)
    return jsonify(resp)      
