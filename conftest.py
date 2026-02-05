from typing import Any, Generator

from playwright.sync_api import sync_playwright, BrowserContext, Playwright
import pytest

@pytest.fixture()
def chromium_context(playwright: Playwright) -> Generator[BrowserContext, Any, None]:
    browser = playwright.chromium.launch(headless=True)
    yield browser.new_context()
    browser.close()

@pytest.fixture()
def authorized_context(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_context(storage_state="browser-state.json")
    browser.close()