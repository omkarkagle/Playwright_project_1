from playwright.sync_api import Page, expect


class dashboard:
           def __init__(self,page:Page):
               self.page = page
               self.dash=page.get_by_role("link",name="Dashboard")


           def is_dashboard_visible(self):
               expect(self.dash).to_be_visible()