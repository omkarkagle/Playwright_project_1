from playwright.sync_api import Page, expect


class dashboard:
           def __init__(self,page:Page):
               self.page = page
               self.dash=page.get_by_role("link",name="Dashboard")
               self.welcome=page.get_by_text("Welcome")
               self.logout=page.get_by_role("link",name="Logout")
               self.btn = page.locator("#btnLogin")

               self.admin_menu=page.get_by_role("link",name="Admin")
               self.pim_menu=page.get_by_role("link",name="PIM")
               self.leave_menu=page.get_by_role("link",name="Leave")
               self.time_menu=page.get_by_role("link",name="Time")
               self.recrutment_menu=page.get_by_role("link",name="Recrutment")




           def is_dashboard_visible(self):
               expect(self.dash).to_be_visible()


           def is_welcome_visible(self):
              self.welcome.click()

           def is_logout_visible(self):
               self.logout.click()

           def is_main_visible(self):
               self.admin_menu.is_visible()
               self.pim_menu.is_visible()
               self.leave_menu.is_visible()
               self.time_menu.is_visible()
               self.recrutment_menu.is_visible()
               self.dash.is_visible()

