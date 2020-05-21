from model.project import Project


def test_add_project(app, json_projects):
    project = json_projects
    old_projects = app.project.get_project_list()
    app.project.create(project)
    assert len(old_projects) + 1 == app.project.count()
    new_projects = app.project.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)

