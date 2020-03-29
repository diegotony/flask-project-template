import yaml
import errno
import os
from workspace import create_workspace,create_directories, create_dir, create_files, create_file


with open('yamls/init.yml', 'r') as f:
    init_file = yaml.load(f, Loader=yaml.FullLoader)

with open('yamls/app.yml', 'r') as f:
    app_file = yaml.load(f, Loader=yaml.FullLoader)


with open('yamls/main.yml', 'r') as f:
    main_file = yaml.load(f, Loader=yaml.FullLoader)

with open('yamls/project_template.yaml', 'r') as f:
    project = yaml.load(f, Loader=yaml.FullLoader)

# def create_app(name):
#     try:
#         create_dir(name)
#         create_directories(name,yaml_data(data,"proyect_structure","init","directory"))
#     except OSError as e :
#         if e.errno != errno.EEXIST:
#             raise
#         pass


def create_project(name):
    create_workspace(project)
    # create_dir(name)
    # create_directories(name, init_file['directory'])
    # create_files(name, init_file['files'])

    # for i in init_file['directory']:
    #     if i == "app":
    #         for j in app_file['directory']:
    #             print(j)
    #             create_directories(name+"/"+"app", app_file['directory'])
    #             create_files(name+"/"+"app", app_file['files'])
    #             if j == "main":
    #                 for k, v in main_file['directory'].items():
    #                     path = name+"/"+"app"+"/"+"main"+"/"
    #                     create_dir(path+k)
    #                     for fi in v:
    #                         create_file(path+k+"/"+fi)


def yaml_data(data, first, second, third):
    return data[first][second][third]


# TODO create_dirs
# TODO create_files
