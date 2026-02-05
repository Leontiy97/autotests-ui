from playwright.sync_api import Page, expect
import pytest

@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):
    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(title).to_be_visible()
    expect(title).to_have_text("Courses")

    icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(icon).to_be_visible()

    no_results = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(no_results).to_be_visible()
    expect(no_results).to_have_text("There is no results")

    result_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(result_text).to_be_visible()
    expect(result_text).to_have_text("Results from the load test pipeline will be displayed here")