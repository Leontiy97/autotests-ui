import pytest
from playwright.sync_api import Playwright, Page

@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_field = page.get_by_test_id("registration-form-email-input").locator("input")
    email_field.fill("user@mail.com")

    username_field = page.get_by_test_id("registration-form-username-input").locator("input")
    username_field.fill("user-user")

    password_field = page.get_by_test_id("registration-form-password-input").locator("input")
    password_field.fill("pass-pass")

    reg_button = page.get_by_test_id("registration-page-registration-button")
    reg_button.click()

    page.wait_for_url("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard")

    context.storage_state(path="courses-browser-state.json")
    browser.close()

@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="courses-browser-state.json")
    yield context.new_page()
    browser.close()