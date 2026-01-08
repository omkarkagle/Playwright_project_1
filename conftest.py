from playwright.sync_api import sync_playwright
from pytest_playwright.pytest_playwright import browser


def page():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=True)
        context=browser.new_context()
        page=context.new_page()
        yield page
        browser.close()
