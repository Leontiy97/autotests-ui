from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.mark.regression
@pytest.mark.authorization
def test_wrong_email_or_password_authorization():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

        email_input = page.locator('//div[@data-testid="login-form-email-input"]//div//input')
        email_input.fill("user.name@gmail.com")

        password_input = page.locator('//div[@data-testid="login-form-password-input"]//div//input')
        password_input.fill("password")

        login_button = page.locator('//button[@data-testid="login-page-login-button"]')
        login_button.click()

        check_validation_text = page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
        expect(check_validation_text).to_be_visible()
        expect(check_validation_text).to_have_text("Wrong email or password")