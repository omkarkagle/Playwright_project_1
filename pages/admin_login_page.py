from textwrap import fill


class AdminLoginPage:
    def __init__(self,page):
        self.page=page
        
    def open(self):
        self.page.goto("http://orangehrm.qedgetech.com/")

    def login(self):
        self.username.fill("user")
        self.password.fill("pass")
        self.button.click()