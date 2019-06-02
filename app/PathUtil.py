import sys

project_name = "flask-adminlte-scaffold"


def getRootDir():
    path = sys.path[0]
    find = path.find("%s" % project_name)
    root_dir = path[:find + len(project_name)]
    return root_dir
