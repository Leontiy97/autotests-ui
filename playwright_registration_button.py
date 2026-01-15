from playwright.sync_api import sync_playwright, expect


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    expect(reg_button).to_be_disabled()

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.focus()
    page.keyboard.type("user.name@gmail.com", delay=200)

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.focus()
    page.keyboard.type("username", delay=200)

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.focus()
    page.keyboard.type("password", delay=200)

    expect(reg_button).to_be_enabled()

    page.wait_for_timeout(1000)