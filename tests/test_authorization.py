from playwright.sync_api import sync_playwright, expect, Page
import pytest

creds = [
    ("user.name@gmail.com", "password"),
    ('user.name@gmail.com', "  "),
    ("  ", "password")
]

@pytest.mark.regression
@pytest.mark.authorization
@pytest.mark.parametrize("email, password", creds)
def test_wrong_email_or_password_authorization(chromium_page: Page, email: str, password: str):
    chromium_page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login")

    email_input = chromium_page.locator('//div[@data-testid="login-form-email-input"]//div//input')
    email_input.fill(email)

    password_input = chromium_page.locator('//div[@data-testid="login-form-password-input"]//div//input')
    password_input.fill(password)

    login_button = chromium_page.locator('//button[@data-testid="login-page-login-button"]')
    login_button.click()

    check_validation_text = chromium_page.locator('//div[@data-testid="login-page-wrong-email-or-password-alert"]')
    expect(check_validation_text).to_be_visible()
    expect(check_validation_text).to_have_text("Wrong email or password")
