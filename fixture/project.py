from model.project import Project


class ProjectHelper:
    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.go_to_manage_page()
        self.go_to_managers_project_page()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        # fill group form
        self.enter_value(project)
        # submit group creation
        wd.find_element_by_xpath("//input[@value='Add Project']").click()
        self.project_cache = None

    def go_to_managers_project_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_link_text("Manage Projects").click()

    def go_to_manage_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_overview_page.php"):
            wd.find_element_by_link_text("Manage").click()

    def delete_project_by_name(self, name):
        wd = self.app.wd
        self.go_to_manage_page()
        self.go_to_managers_project_page()
        # select
        self.select_project_by_name(name)
        # submit
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.implicitly_wait(2)
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        self.project_cache = None

    def select_project_by_name(self, name):
        wd = self.app.wd
        wd.find_element_by_link_text("%s" % name).click()

    def enter_value(self, project):
        self.change_field_value("name", project.name)
        self.change_field_value("description", project.description)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.go_to_manage_page()
        self.go_to_managers_project_page()
        tables = wd.find_elements_by_xpath("//table[@class='width100']")
        table = tables[1]
        rows_count = len(table.find_elements_by_tag_name("tr"))
        return rows_count-2

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.wd
            self.project_cache = []

            self.go_to_manage_page()
            self.go_to_managers_project_page()
            tables = wd.find_elements_by_xpath("//table[@class='width100']")
            table = tables[1]
            rows = table.find_elements_by_tag_name("tr")
            del rows[0:2]
            for row in rows:
                cells = row.find_elements_by_tag_name("td")
                name = cells[0].text
                description = cells[4].text
                id = cells[0].find_element_by_tag_name("a").get_attribute("href")[75:]
                pr = Project(name=name, description=description, id=id)
                self.project_cache.append(pr)
        return list(self.project_cache)
