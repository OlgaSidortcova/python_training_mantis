from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.mail import MailHelper
from fixture.signup import SignupHelper



class Application:
    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognised browser %s" % browser)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.wd.implicitly_wait(5)
        self.session = SessionHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.project = ProjectHelper(self)


    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()
