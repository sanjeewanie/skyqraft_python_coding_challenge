from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.config import Config
from flask_mysqldb import MySQL


mysql = MySQL()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

  
   
    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = ''
    app.config['MYSQL_DB'] = 'crud_assignmnet'
 
    mysql.init_app(app)

    from src.users.routes import users
    from src.project.routes import projects
    from src.user_group.routes import groups
    from src.main.routes import main
    app.register_blueprint(users)
    app.register_blueprint(projects)
    app.register_blueprint(groups)
    app.register_blueprint(main)

    return app
