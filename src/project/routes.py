from flask import jsonify, render_template, request, Blueprint
from src import mysql
from src.models import get_projects, get_project_by_name, insert_project, update_project_by_name, delete_project_by_name

projects = Blueprint('projects', __name__,url_prefix='/project')

# ex: GET http://127.0.0.1:5000/project
@projects.route("/", methods=['GET'])
def list_projects():
    # get the list of all projects from db and return json
    projects = get_projects();
    return jsonify(projects)
    

# ex: POST http://127.0.0.1:5000/project     Add the project model3
#{
# "name":"model3",
# "type":"internal",
# "description":"description of project"
# }
@projects.route("/", methods=['POST'])
def create_project():
    data=request.get_json(force=True)
    # save project to db
    resp=insert_project(data)
    return jsonify(resp)


# ex: GET http://127.0.0.1:5000/project/model3
@projects.route("/<string:name>", methods=['GET'])
def get_project(name):
    # get the details of the project by 'name' from db and return it as json
    project = get_project_by_name(name)
    return jsonify(project)


# ex: POST http://127.0.0.1:5000/project/model3
@projects.route("/<string:name>", methods=['POST'])
def update_project(name):
    data=request.get_json(force=True)
    # update the details of the project by 'name' with data and return it as json
    resp=update_project_by_name(name, data)
    return jsonify(resp)


# ex: DELETE http://127.0.0.1:5000/project/model3     Delete the project model3
@projects.route("/<string:name>", methods=['DELETE'])
def delete_project(name):
    # delete project by 'name'
    resp=delete_project_by_name(name)
    return jsonify(resp)