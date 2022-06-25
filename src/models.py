from datetime import datetime
from re import U
import MySQLdb
from itsdangerous import Serializer
from src import mysql


# users
def get_users():
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    csr.execute('SELECT * FROM users')
    try:
        users = csr.fetchall()
        csr.close()
        return users ,{"status":200}
    except:
        return 'bad request!', 400  



def get_user_by_name(name):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "SELECT * FROM users WHERE name='%s'" %(name,)
    
    try:
        csr.execute(cmd)
        user = csr.fetchall()
        csr.close()
        return user[0] if user else {} 
    except:
        return 'bad request!', 400


def get_user_all_details_by_name(name):
    data={}
    user = get_user_by_name(name)    
    print("user")
    print(user)

    user_group = get_group_by_username(name)
    print("user_group")
    print(user_group)

    user_projects = get_project_by_username(name)

    print("user_projects")
    print(user_projects)
   

    data['user']=user
    data['user_group']=user_group
    data['user_projects']=user_projects

    return data   

def get_user_by_groupname(name):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "SELECT u.* FROM groups g join user_group ug on g.id=ug.user_group join users u on u.id=ug.user_id WHERE g.name='%s'" %(name,)
    try:
        csr.execute(cmd)
        user = csr.fetchall()
        csr.close()
        return user if user else {} 
    except:
        return 'bad request!', 400    

def insert_user(data):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "INSERT into users (name, email, status, title) VALUES ('%s', '%s', '%s', '%s')" %(data['name'],
                                                                                            data['email'],
                                                                                            data['status'],
                                                                                            data['title'])
    
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "User Saved Sucssessfully ",{"status":200}
    except:
        return 'bad request!', 400 

def update_user_by_name(name, data):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cmd= "UPDATE users SET name = '%s', email = '%s', status='%s', title= '%s' WHERE name = '%s'"% (data['name'],
                                                                                                    data['email'],
                                                                                                    data['status'],
                                                                                                    data['title'],
                                                                                                    name)

     
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "User Updated Sucssessfully ",{"status":200}
    except:
        return 'bad request!', 400 

def deleter_user_by_name(name):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "DELETE FROM users WHERE name = '%s'" % (name,)
    
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "User Deleted Sucssessfully ",{"status":200}
    except:
        return 'bad request!', 400



# projects
def get_projects():
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    csr.execute('SELECT * FROM projects')
    try:
        projects = csr.fetchall()
        csr.close()
        return projects
    except:
        return 'bad request!', 400

def get_project_by_name(name):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "SELECT * FROM projects WHERE name='%s'" %(name,)
    
    try:
        csr.execute(cmd)
        project = csr.fetchall()
        csr.close()
        return project[0] if project else {} 
    except:
        return 'bad request!', 400

def insert_project(data):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "INSERT into projects (name, type, description) VALUES ('%s', '%s', '%s')" %(data['name'],
                                                                                            data['type'],
                                                                                            data['description'])
    
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "Project Saved Succesfully "
    except:
        return 'bad request!', 400

def update_project_by_name(name, data):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    cmd= "UPDATE projects SET name = '%s', type = '%s', description='%s' WHERE name = '%s'"% (data['name'],
                                                                                                    data['type'],
                                                                                                    data['description'] ,name)
                                                                                                    
      
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "Project Updated Succesfully "
    except:
        return 'bad request!', 400

def delete_project_by_name(name):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "DELETE FROM projects WHERE name = '%s'" % (name,)
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "Project Deleted Succesfully ",{"status":200}
    except:
        return 'bad request!', 400


def get_project_by_username(name):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "SELECT p.name as project_name,r.name as role_name FROM `project_user` pu \
                join users u \
                on u.id=pu.user_id\
                join projects p \
                on p.id=pu.project_id\
                join roles r \
                on r.id=pu.project_role\
                where u.name='%s' \
                group by p.id,pu.project_role" % (name,)
    
    
    try:
        csr.execute(cmd)
        project = csr.fetchall()
        csr.close()
        return project if project else {} 
    except:
        return 'bad request!', 400

def get_project_by_groupname(name):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "SELECT p.name as project_name,r.name as role_name FROM `project_user` pu \
                join users u \
                on u.id=pu.user_id\
                join projects p \
                on p.id=pu.project_id\
                join roles r \
                on r.id=pu.project_role\
                where u.name='%s' \
                group by p.id,pu.project_role" % (name)
    
    
    try:
        csr.execute(cmd)
        project = csr.fetchall()
        csr.close()
        return project if project else {} 
    except:
        return 'bad request!', 400     






# groups
def get_groups():
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    csr.execute('SELECT * FROM groups')
    
    try:
        groups = csr.fetchall()
        csr.close()
        return groups,{"status":200}
    except:
        return 'bad request!', 400


def get_group_all_details_by_name(name):
    data={}
    user = get_user_by_groupname(name)    
    print("user")
    print(user)   

    user_projects = get_project_by_groupname(name)

    print("user_projects")
    print(user_projects)
   

    data['user']=user
    data['user_projects']=user_projects

    return data


def get_group_by_name(name):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "SELECT * FROM groups WHERE name='%s'" %(name,)
    
    try:
        csr.execute(cmd)
        group = csr.fetchall()
        #print(group)
        csr.close()
        return group[0] if group else {}
    except:
        return 'bad request!', 400


def get_group_by_username(name):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "SELECT g.name as group_names FROM groups g join user_group ug on g.id=ug.user_group join users u on u.id=ug.user_id WHERE u.name='%s'" %(name,)
    
    try:
        csr.execute(cmd)
        group = csr.fetchall()
        csr.close()
        return group if group else {}
    except:
        return 'bad request!', 400    

def insert_group(data):
    print(data)
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "INSERT into groups (name) VALUES ('%s')" %(data['name'])
    
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "Group Saved Succesfully"
    except:
        return 'bad request!', 400 

def update_group_by_name(name, data):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd= "UPDATE groups SET name = '%s' WHERE name = '%s'"% (data['name'], name)     
    
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "Group Updated Succesfully",{"status":200}
    except:
        return 'bad request!', 400

def delete_group_by_name(name):
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "DELETE FROM groups WHERE name = '%s'" % (name,)
   
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "Group Deleted Succesfully",{"status":200}
    except:
        return 'bad request!', 400




# Project roles
def get_role_by_name(name):
    
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "SELECT * FROM roles WHERE name='%s'" %(name)
    
    try:
        csr.execute(cmd)
        role = csr.fetchall()
        csr.close()
        return role[0] if role else {}
    except:
        return 'bad request!', 400



#assignments
def get_all_assignments():
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    sql = "SELECT u.name as username,g.name as group_name ,p.name as project_name , r.name as role_name \
            FROM `user_group` ug\
            join users u \
            on ug.user_id=u.id\
            join groups g\
            on g.id=ug.user_group\
            join project_user pu \
            on pu.user_id=u.id\
            left join projects p \
            on p.id=pu.project_id\
            join roles r \
            on r.id=pu.project_role;"
       
    try:
        csr.execute(sql)
        project_assignments = csr.fetchall()
        csr.close()
        return project_assignments ,{"status":200}
    except:
        return 'bad request!', 400
    

def insert_user_assignments(data):
    
    user_id=get_user_by_name(data['name'])['id']
   
    project_id=get_project_by_name(data['project'])['id']
   
    role_id=get_role_by_name(data['role'])['id']
    
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "INSERT into project_user (user_id, project_id, project_role) VALUES ('%s', '%s', '%s')" %(user_id,
                                                                                            project_id,
                                                                                            role_id
                                                                                            )
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "Project User Assignment Saved successfully "
    except:
        return 'bad request!', 400

def insert_group_assignments(data):

    user_id=get_user_by_name(data['user'])['id']
    user_group_id=get_group_by_name(data['name'])['id']
    csr = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cmd = "INSERT  into user_group (user_id,user_group) VALUES ('%s', '%s')" %(user_id, user_group_id)
    try:
        csr.execute(cmd)
        mysql.connection.commit()
        csr.close()
        return "User Group Assignment Saved successfully" 
    except:
        return 'bad request!', 400    

def insert_project_assignments(data):
    
    users=get_user_by_groupname(data['group'])
    
    try:
        for user in users:
            assign_data={} 
            assign_data['name']=user['name']
            assign_data['project']=data['name']
            assign_data['role']=data['role']
            
            insert_user_assignments(assign_data)
           
        return "Group Assignment Saved successfully " 
    except:
        return 'bad request!', 400    
