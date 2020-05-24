from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        url = self.app.base_url
        client = Client(url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False


    def get_project_list(self, username, password):
        url = self.app.base_url
        project_list = []
        client = Client(url + "/api/soap/mantisconnect.php?wsdl")
        try:
            project_list = client.service.mc_projects_get_user_accessible(username, password)
        except WebFault:
            pass
        projects = []
        for project in project_list:
            projects.append(Project(name=project.name, id=project.id, description=project.description))
        return projects
