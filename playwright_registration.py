from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    expect(email_input).to_be_visible()
    email_input.fill('user.name@gmail.com')

    name_input = page.get_by_test_id('registration-form-username-input').locator('input')
    expect(name_input).to_be_visible()
    name_input.fill('username')

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    expect(password_input).to_be_visible()
    password_input.fill('password')

    reg_button = page.get_by_test_id('registration-page-registration-button')
    expect(reg_button).to_be_visible()
    reg_button.click()

    page.wait_for_url('**/#/dashboard')
    dashboard_panel = page.get_by_test_id('dashboard-toolbar-title-text')
    expect(dashboard_panel).to_be_visible()
    expect(dashboard_panel).to_have_text('Dashboard')

    # page.wait_for_timeout(1000)