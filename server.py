import os

from bottle import Bottle, run
from git import Repo

app = Bottle()

repo = Repo(path=os.getcwd())


@app.route('/')
def index():
    return "hello, world!"


@app.route('/info')
def info():
    return {
        'service_name': 'myapplication',
        'version': '1.0.0',
        'git_commit_sha': repo.head.object.hexsha,
        'environment': {
            'service_port': int(os.getenv('SERVICE_PORT', 5000)),
            'log_level': os.getenv('LOG_LEVEL', 'INFO')
        }
    }


run(app, host='0.0.0.0', port=os.getenv('SERVICE_PORT', 8080))
