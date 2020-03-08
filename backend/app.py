from flask import Flask, jsonify, request
from flask_cors import CORS
import uuid
DEBUG = True

PROJECTS = [
    {   'id': uuid.uuid4().hex,
        'title': 'Chameleon',
        'info': 'CryptoConsole',
        'url': 'https://sun9-49.userapi.com/c847216/v847216719/195540/eIkZwdRGdRY.jpg'
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Chameleon',
        'info': 'CryptoConsole',
        'url': 'https://sun9-49.userapi.com/c847216/v847216719/195540/eIkZwdRGdRY.jpg'
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Chameleon',
        'info': 'CryptoConsole',
        'url': 'https://sun9-49.userapi.com/c847216/v847216719/195540/eIkZwdRGdRY.jpg'
    },
    {   'id': uuid.uuid4().hex,
        'title': 'Chameleon',
        'info': 'CryptoConsole',
        'url': 'https://sun9-49.userapi.com/c847216/v847216719/195540/eIkZwdRGdRY.jpg'
    },
]

def remove_project(project_id):
    for project in PROJECTS:
        if project['id'] == project_id:
            PROJECTS.remove(project)
            return True
    return False

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/projects', methods=['GET','POST'])
def get_projects():
    responce_object = {'status': 'success'}
    if request.method == 'POST':
        post_data =request.get_json()
        PROJECTS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'info': post_data.get('info'),
            'url': post_data.get('url')
        })
        responce_object['message'] = 'Project added!'
    else:
        responce_object['projects'] = PROJECTS
    return jsonify(responce_object)

@app.route('/projects/<project_id>', methods=['PUT', 'DELETE'])
def single_book(project_id):
    responce_object = {'status' : 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_project(project_id)
        PROJECTS.append({
            'id':  uuid.uuid4().hex,
            'title': post_data.get('title'),
            'info': post_data.get('info'),
            'url': post_data.get('url')
        })
        responce_object['message'] = 'Project updated!'
    if request.method == 'DELETE':
        remove_project(project_id)
        responce_object['message'] = 'Project removed'
    return jsonify(responce_object)

if __name__ == '__main__':
    app.run()
