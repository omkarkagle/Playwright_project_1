
from playwright.sync_api import Page, expect


class pimPage:
    def __init__(self,page:Page):
        self.page=page

        self.pim_menu=page.get_by_role("link",name="PIM")
        self.add_emp=page.get_by_role("link",name="Add Employee")

        self.f_name=page.locator("#firstName")
        self.l_name=page.locator("#lastName")
        self.btn=page.get_by_role("button",name="Save")

        self.page_title = page.get_by_role("heading", name="Personal Details")


    def open_pim(self):
        self.pim_menu.click()

    def open_add_emp(self):
        self.add_emp.click()

    def addd_emp(self):
        self.f_name.fill("ajeet")
        self.l_name.fill("bhaiyaa")
        self.btn.click()

    def is_emp_displayed(self):
        expect(self.page_title).to_be_visible()