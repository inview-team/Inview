import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from model import db,init_db, ProjectsInfo, User


DEBUG = True

load_dotenv(find_dotenv())

application = Flask(__name__)
application.config.from_object(__name__)

CORS(application, resources={r'/*': {'origins': '*'}})



database_uri = 'mysql+pymysql://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
    dbuser=os.environ['DBUSER'],
    dbpass=os.environ['DBPASS'],
    dbhost=os.environ['DBHOST'],
    dbname=os.environ['DBNAME']
)

application.config.update(
    SQLALCHEMY_DATABASE_URI=database_uri,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db.init_app(application)
with application.app_context():
    init_db()

@application.route('/projects', methods=['GET','POST'])
def get_projects():
    if request.method == 'POST':
        title=str(request.json.get('title'))
        info=str(request.json.get('info'))
        image_url=str(request.json.get('url'))

        project_request = ProjectsInfo(id=None,title=title, info=info, image_url=image_url)
        db.session.add(project_request)
        db.session.commit()

        return jsonify({'message':'Project added!'})
    else:
        records = ProjectsInfo.query.all()
        return jsonify({'projects':[record.serialize() for record in records]})

@application.route('/projects/<project_id>', methods=['PUT', 'DELETE'])
def single_project(project_id):
    responce_object = {'status' : 'success'}
    if request.method == 'PUT':
        responce=request.get_json()
        id=int(project_id)

        project = ProjectsInfo.query.get(project_id)
        project.title=responce['title']
        project.info=responce['info']
        project.image_url=responce['url']
        db.session.commit()

        return jsonify({'message':'Project updated!'})
    if request.method == 'DELETE':
        project = ProjectsInfo.query.get(project_id)
        db.session.delete(project)
        db.session.commit()
        responce_object['message'] = 'Project removed'
    return jsonify(responce_object)

@application.route('/check/<login>', methods=['GET'])
def check(login):
    user = User.query.get(login)
    if user != None:
        if user.isAdmin == 1:
            return jsonify({'isAdmin': True})
        else:
            return jsonify({'isAdmin': False})
    else:
        return jsonify({'isAdmin': False})


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
