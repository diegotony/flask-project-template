import errno
import os


def create_files(name, files):
    for i in files:
        create_file(name+"/"+i)


def create_file(path):
    open(path, 'w+')


def create_directories(path, directories):
    for dir in directories:
        f = create_dir(path+"/"+dir)


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
            create_file(path+"/"+i)


def check_str(test, path):
    if type(test) is str:
        create_file(path+"/"+test)


def create_workspace(yaml_file):
    for name_app, structure in yaml_file.items():
        create_dir(name_app)
        check_list(structure, name_app)
        check_str(structure, name_app)
        if check_dict(structure) is True:
            for folder, files in structure.items():
                check_list(files, name_app)
                check_str(files, name_app)
                if check_dict(files) is True:
                    create_dir(name_app+"/"+folder)
                    for d, r in files.items():
                        create_dir(name_app+"/"+folder)
                        check_list(r, name_app+"/"+folder)
                        check_str(r, name_app+"/"+folder)
                        if check_dict(r) is True:
                            create_dir(name_app+"/"+folder+"/"+d)
                            for q, w in r.items():
                                create_dir(name_app+"/"+folder+"/"+d+"/"+q)
                                check_list(w,name_app+"/"+folder+"/"+d+"/"+q)
                                check_str(w,name_app+"/"+folder+"/"+d+"/"+q)

        # * create main directory
        # * check if is list or dict
