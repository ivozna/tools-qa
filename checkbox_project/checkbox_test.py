def test_checkbox(checkbox_page):
    checkbox_page.toggle('Home')
    checkbox_page.toggle('Documents')
    checkbox_page.check_menu('Office')
    assert checkbox_page.check_selected(["office", "public", "private", "classified", "general"])
    assert checkbox_page.get_size() == 5
    checkbox_page.close()


def test_checkbox_and_uncheck(checkbox_page):
    checkbox_page.check_menu('Home')
    checkbox_page.toggle('Home')
    checkbox_page.check_menu('Documents')
    checkbox_page.check_menu('Downloads')
    assert checkbox_page.check_selected(["desktop", "notes", "commands"])
    assert checkbox_page.get_size() == 3
    checkbox_page.close()





"""Test case
Steps
1. Go to page
2. Expend Home
3. Expend documents
4. Check office

Expected result:
"You have selected : office, public, private, classified, general" is printed.
"""

"""from playwright.sync_api import Playwright, sync_playwright

expected_items = ["office", "public", "private", "classified", "general"]


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://demoqa.com/checkbox")

    page.click('button:left-of(:text("Home"))')
    page.click('button:left-of(:text("Documents"))')
    page.click('.rct-checkbox:left-of(:text("Office"))')

    result = page.query_selector('#result').inner_text()
    for item in expected_items:
        assert item in result

    assert len(page.query_selector_all('#result .text-success')) == len(expected_items)

    page.close()
    context.close()
    browser.close()


def test_checkbox():
    with sync_playwright() as playwright:
        run(playwright)"""
