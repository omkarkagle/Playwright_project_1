from textwrap import fill

from playwright.sync_api import Page, expect


class AdminLoginPage:
    def __init__(self,page:Page):
        self.page=page
        self.username= page.locator("#txtUsername")
        self.password=page.locator("#txtPassword")
        self.btn=page.locator("#btnLogin")
        self.error_msg = page.locator("#spanMessage")


    def enter_username(self,username:str):
        self.username.fill(username)

    def enter_password(self,password:str):
        self.password.fill(password)

    def enter_btn(self):
        self.btn.click()

    def login(self,username:str,password:str):
        self.enter_username(username)
        self.enter_password(password)
        self.enter_btn()

