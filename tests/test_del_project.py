from model.project import Project
import random


def test_delete_some_project(app):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    projects_before = app.soap.get_project_list(username, password)
    if len(projects_before) == 0:
        project = Project(name="test1")
        app.project.create(project)
        projects_before.append(project)
    project = random.choice(projects_before)
    app.project.delete_project_by_name(project.name)
    projects_after = app.soap.get_project_list(username, password)
    assert len(projects_before) - 1 == len(projects_after)
    projects_before.remove(project)
    assert sorted(projects_before, key=Project.id_or_max) == sorted(projects_after, key=Project.id_or_max)
