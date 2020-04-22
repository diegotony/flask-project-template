import yaml
import errno
import os
from flask_project_template.workspace import create_workspace, create_directories, create_dir, create_files, create_file


with open('flask_project_template/yamls/init.yml', 'r') as f:
    init_file = yaml.load(f, Loader=yaml.FullLoader)

with open('flask_project_template/yamls/app.yml', 'r') as f:
    app_file = yaml.load(f, Loader=yaml.FullLoader)


with open('flask_project_template/yamls/main.yml', 'r') as f:
    main_file = yaml.load(f, Loader=yaml.FullLoader)

with open('flask_project_template/yamls/project_template.yaml', 'r') as f:
    project = yaml.load(f, Loader=yaml.FullLoader)


def create_project(name):
    create_workspace(project, name)


def yaml_data(data, first, second, third):
    return data[first][second][third]

def hello_world():
    return "holi"

# TODO create_dirs
# TODO create_files
