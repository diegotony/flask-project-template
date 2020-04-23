import os
from flask_project_template.utils.jinja_utils import render_template


def create_files(name, files):
    for i in files:
        create_file_jinja(name + "/" + i, i)


def create_file(path):
    open(path, 'w+')


def create_file_jinja(path, name):
    print(name)
    with open(path, 'w+') as file:
        file.write(render_template(name))


def create_directories(path, directories):
    for directory in directories:
        create_dir(path + "/" + directory)


def create_dir(path):
    return os.makedirs(path, exist_ok=True)


def check_dict(test):
    if type(test) is dict:
        return True
    else:
        return False


def check_list(test, path):
    if type(test) is list:
        for i in test:
            create_file_jinja(path + "/" + i, i)


def check_str(test, path):
    if type(test) is str:
        create_file_jinja(path + "/" + test, test)



