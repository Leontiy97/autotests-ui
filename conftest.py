from playwright.sync_api import sync_playwright, expect
import pytest

@pytest.fixture()
def context():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()

        yield context

        context.close()
        browser.close()

@pytest.fixture()
def authorized_context():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")

        yield context

        context.close()
        browser.close()