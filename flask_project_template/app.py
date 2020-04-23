import yaml
from jinja2 import Template
from flask_project_template.generators.flask_workspace import create_workspace_directory
from flask_project_template.utils.jinja_utils import render_template

with open('flask_project_template/yamls/flask/project_template.yaml', 'r') as f:
    project = yaml.load(f, Loader=yaml.FullLoader)


def create_project(name):
    create_workspace_directory(project, name)


def tem():
    print(render_template('requirements.txt'))
