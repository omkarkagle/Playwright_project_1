from hrms.conftest import page
from playwright.sync_api import expect, Page
from hrms.pages.admin_login_page import AdminLoginPage
from hrms.pages.dashboard import dashboard



def test_admin_login(page:Page):
    login_Page=AdminLoginPage(page)
    dashhh=dashboard(page)

    page.goto("http://orangehrm.qedgetech.com")
    login_Page.enter_username("Admin")
    login_Page.enter_password("Qedge123!@#")
    login_Page.enter_btn()
    dashhh.is_dashboard_visible()
