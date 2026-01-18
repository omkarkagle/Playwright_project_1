from playwright.sync_api import Page
from hrms.pages.admin_login_page import AdminLoginPage
from hrms.pages.pim_page import pimPage


def test_add_emp(page:Page):
    login= AdminLoginPage(page)
    pim= pimPage(page)

    page.goto("http://orangehrm.qedgetech.com")
    login.enter_username("admin")
    login.enter_password("Qedge123!@#")
    login.enter_btn()

    pim.open_pim()
    pim.open_add_emp()
    pim.addd_emp()

    pim.is_emp_displayed()
