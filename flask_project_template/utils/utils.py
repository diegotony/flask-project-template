import yaml

from flask_project_template.workspace import create_workspace, create_directories, create_dir, create_files, create_file

with open('flask_project_template/yamls/project_template.yaml', 'r') as f:
    project = yaml.load(f, Loader=yaml.FullLoader)


def create_project(name):
    create_workspace(project, name)


def hello_world():
    return "holi"
