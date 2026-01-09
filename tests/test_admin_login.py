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

def test_login_with_invalid_credentials(page:Page):
    login_Page=AdminLoginPage(page)


    page.goto("http://orangehrm.qedgetech.com")

    login_Page.enter_username("Admin")
    login_Page.enter_password("xxxx")
    login_Page.enter_btn()

    expect(login_Page.error_msg).to_be_visible()
    expect(login_Page.error_msg).to_have_text("Invalid credentials")

def test_login_with_empty_username(page:Page):
    login_Page=AdminLoginPage(page)


    page.goto("http://orangehrm.qedgetech.com")

    login_Page.enter_username("")
    login_Page.enter_password("xxxx")
    login_Page.enter_btn()

    expect(login_Page.error_msg).to_be_visible()
    expect(login_Page.error_msg).to_have_text("Username cannot be empty")

def test_login_with_empty_password(page:Page):
    login_Page=AdminLoginPage(page)


    page.goto("http://orangehrm.qedgetech.com")

    login_Page.enter_username("Admin")
    login_Page.enter_password("")
    login_Page.enter_btn()

    expect(login_Page.error_msg).to_be_visible()
    expect(login_Page.error_msg).to_have_text("Password cannot be empty")


def test_login_with_both_empty(page:Page):
    login_Page=AdminLoginPage(page)


    page.goto("http://orangehrm.qedgetech.com")

    login_Page.enter_username("")
    login_Page.enter_password("")
    login_Page.enter_btn()

    expect(login_Page.error_msg).to_be_visible()
    expect(login_Page.error_msg).to_have_text("Username cannot be empty")
