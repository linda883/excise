import os


def file_path():
    root_path = os.path.dirname(os.path.abspath(__file__))
    # print(root_path)
    project_path = root_path[:root_path.rfind("excise") + len("excise")]
    # print(project_path)
    return project_path
