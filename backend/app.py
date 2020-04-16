import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, jsonify, request
from flask_cors import CORS
from model import db, init_db, ProjectsInfo, User

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


@application.route('/projects', methods=['GET', 'POST'])
def get_projects():
    if request.method == 'POST':
        try:
            title = str(request.json.get('title'))
            info = str(request.json.get('info'))
            image_url = str(request.json.get('url'))

            project_request = ProjectsInfo(id=None, title=title, info=info, image_url=image_url)
            db.session.add(project_request)
            db.session.commit()
            return jsonify({'message': 'Project added!'})
        except:
            print('Error with POST')
    else:
        try:
            records = ProjectsInfo.query.all()
            return jsonify({'projects': [record.serialize() for record in records]})
        except:
            print('Error with GET')


@application.route('/projects/<project_id>', methods=['PUT', 'DELETE'])
def single_project(project_id):
    responce_object = {'status': 'success'}
    if request.method == 'PUT':
        try:
            responce = request.get_json()
            project = ProjectsInfo.query.get(project_id)
            project.title = responce['title']
            project.info = responce['info']
            project.image_url = responce['url']
            db.session.commit()
            return jsonify({'message': 'Project updated!'})
        except:
            print('Error with PUT')
    elif request.method == 'DELETE':
        try:
            project = ProjectsInfo.query.get(project_id)
            db.session.delete(project)
            db.session.commit()
            responce_object['message'] = 'Project removed'
            return jsonify(responce_object)
        except:
            print('Error with DELETE')


if __name__ == "__main__":
    application.run(host="0.0.0.0", port=5000)
