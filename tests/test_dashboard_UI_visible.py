from playwright.sync_api import Page
from hrms.pages.admin_login_page import AdminLoginPage
from hrms.pages.dashboard import dashboard


def test_dashboard_UI_visible(page:Page):
    Login_Page=AdminLoginPage(page)
    dashh=dashboard(page)

    page.goto("http://orangehrm.qedgetech.com")

    Login_Page.enter_username("admin")
    Login_Page.enter_password("Qedge123!@#")
    Login_Page.enter_btn()


    dashh.is_main_visible()


