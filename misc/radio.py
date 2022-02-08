"""Test case
Steps
1. Go to page
2. Click "Yes"
3. Check if - "You have selected Yes" is printed.
4. Click "Impressive"
5. Check if - "You have selected Impressive" is printed.
6. Click "No"
7. Check if - "You have selected Impressive" is printed."""

from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demoqa.com/radio-button")

    page.check(".custom-control-label[for='yesRadio']")
    assert page.query_selector("text=You have selected Yes")

    page.check(".custom-control-label[for='impressiveRadio']")
    assert page.query_selector("text=You have selected Impressive")

    assert page.query_selector("text=You have selected Impressive")

    assert page.is_disabled('#noRadio') is True

    page.close()
    context.close()
    browser.close()


def test_radio():
    with sync_playwright() as playwright:
        run(playwright)
