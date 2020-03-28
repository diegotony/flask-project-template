import yaml
import errno
import os

with open('ymals/init.yml','r') as f:
    init = yaml.load(f,Loader=yaml.FullLoader)

with open('ymals/app.yml','r') as f:
    app = yaml.load(f,Loader=yaml.FullLoader)

# def create_app(name):
#     try:
#         create_dir(name)
#         create_directories(name,yaml_data(data,"proyect_structure","init","directory"))
#     except OSError as e :
#         if e.errno != errno.EEXIST:
#             raise
#         pass

def create_project(name):
    create_dir(name)
    create_directories(name,init['directory'])
    create_files(name,init['files'])
    
    for i in init['directory']:
        if i == "app":
            for i in app['directory']:
                print(i)
            # create_directories(name+"/"+i,app['directory'])
            # create_files(name+"/"+i,app['files'])

        

def create_directories(path,directories):
    for dir in directories:
        f= create_dir(path+"/"+dir)


def create_files(name,files):
    for i in files:
        open(name+"/"+i,'w+')

def create_folder():
    pass


def yaml_data(data,first,second,third):
    return data[first][second][third]

def create_dir(path):
    return os.makedirs(path,exist_ok=True)


# TODO create_dirs
# TODO create_files
 



