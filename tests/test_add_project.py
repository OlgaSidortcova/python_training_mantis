from model.project import Project
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):# json_projects):
    #project = json_projects
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    projects_before = app.soap.get_project_list(username, password)
    project = Project(name=random_string("project_", 10), description=random_string("des_", 30))
    app.project.create(project)
    projects_after = app.soap.get_project_list(username, password)
    assert len(projects_before) + 1 == len(projects_after)
    projects_before.append(project)
    assert sorted(projects_before, key=Project.id_or_max) == sorted(projects_after, key=Project.id_or_max)

