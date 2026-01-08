from hrms.conftest import page
from playwright.sync_api import expect

def test_admin_login(page):
    login=test_admin_login(page)
    login.open()
    login.login("Admin","Qedge123!@#")

    expect(page.get_by_text("Dashboard")).to_be_visible()