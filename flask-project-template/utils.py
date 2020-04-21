import yaml
import errno
import os
from workspace import create_workspace,create_directories, create_dir, create_files, create_file


with open('flask-project-template/yamls/init.yml', 'r') as f:
    init_file = yaml.load(f, Loader=yaml.FullLoader)

with open('flask-project-template/yamls/app.yml', 'r') as f:
    app_file = yaml.load(f, Loader=yaml.FullLoader)


with open('flask-project-template/yamls/main.yml', 'r') as f:
    main_file = yaml.load(f, Loader=yaml.FullLoader)

with open('flask-project-template/yamls/project_template.yaml', 'r') as f:
    project = yaml.load(f, Loader=yaml.FullLoader)

def create_project(name):
    create_workspace(project, name)

def yaml_data(data, first, second, third):
    return data[first][second][third]


# TODO create_dirs
# TODO create_files
