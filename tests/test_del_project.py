from model.project import Project
import random


def test_delete_some_project(app):
    if app.project.count() == 0:
        app.project.create(Project(name="test1"))
    old_projects = app.project.get_project_list()

    project = random.choice(old_projects)
    app.project.delete_project_by_name(project.name)
    assert len(old_projects) - 1 == app.project.count()
    old_projects.remove(project)
    new_projects = app.project.get_project_list()
    assert old_projects == new_projects
