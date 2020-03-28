import yaml
import errno
import os

with open('data.yml','r') as f:
    data = yaml.load(f,Loader=yaml.FullLoader)


def get_directories(path,directories):
    for dir in directories:
        create_dir(path+"/"+dir)


def create_app(name):
    try:
        create_dir(name)
        get_directories(name,yaml_data(data,"proyect_structure","init","directory"))
    except OSError as e :
        if e.errno != errno.EEXIST:
            raise
        pass


def yaml_data(data,first,second,third):
    return data[first][second][third]

def create_dir(path):
    return os.makedirs(path,exist_ok=True)

# TODO get_files
# TODO create_dirs
# TODO create_files
 



