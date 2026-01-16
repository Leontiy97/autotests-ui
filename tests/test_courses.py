from playwright.sync_api import sync_playwright, expect

def test_empty_courses_list():
    with sync_playwright() as playwright:
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

    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="courses-browser-state.json")
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        title = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(title).to_be_visible()
        expect(title).to_have_text("Courses")

        icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(icon).to_be_visible()

        no_results = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(no_results).to_be_visible()
        expect(no_results).to_have_text("There is no results")

        result_text = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(result_text).to_be_visible()
        expect(result_text).to_have_text("Results from the load test pipeline will be displayed here")