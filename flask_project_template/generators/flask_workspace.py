import os


def create_files(name, files):
    for i in files:
        create_file(name + "/" + i)


def create_file(path):
    open(path, 'w+')


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
            create_file(path + "/" + i)


def check_str(test, path):
    if type(test) is str:
        create_file(path + "/" + test)


def create_workspace(yaml_file, name):
    for name_app, structure in yaml_file.items():
        name_project = name
        user = os.getenv("USER")
        print(user)
        # os.chdir('/home/{0}/'.format(user))
        create_dir(name_project)
        check_list(structure, name_project)
        check_str(structure, name_project)
        if check_dict(structure) is True:
            for folder, files in structure.items():
                check_list(files, name_project)
                check_str(files, name_project)
                if check_dict(files) is True:
                    create_dir(name_project + "/" + folder)
                    for d, r in files.items():
                        create_dir(name_project + "/" + folder)
                        check_list(r, name_project + "/" + folder)
                        check_str(r, name_project + "/" + folder)
                        if check_dict(r) is True:
                            create_dir(name_project + "/" + folder + "/" + d)
                            for q, w in r.items():
                                create_dir(name_project + "/" + folder + "/" + d + "/" + q)
                                check_list(w, name_project + "/" +
                                           folder + "/" + d + "/" + q)
                                check_str(w, name_project + "/" +
                                          folder + "/" + d + "/" + q)
