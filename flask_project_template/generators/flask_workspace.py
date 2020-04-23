from flask_project_template.utils.utils import *


def create_workspace_directory(yaml_file, name):
    for name_app, structure in yaml_file.items():
        name_project = name
        user = os.getenv("USER")
        os.chdir('/home/{0}/'.format(user))
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
