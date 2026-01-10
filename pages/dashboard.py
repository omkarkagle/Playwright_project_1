from playwright.sync_api import Page, expect


class dashboard:
           def __init__(self,page:Page):
               self.page = page
               self.dash=page.get_by_role("link",name="Dashboard")
               self.welcome=page.get_by_text("Welcome")
               self.logout=page.get_by_role("link",name="Logout")
               self.btn = page.locator("#btnLogin")



           def is_dashboard_visible(self):
               expect(self.dash).to_be_visible()


           def is_welcome_visible(self):
              self.welcome.click()

           def is_logout_visible(self):
               self.logout.click()