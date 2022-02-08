from playwright.sync_api import Playwright, sync_playwright


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=100, devtools=True)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://todomvc.com/examples/vanillajs/")

    page.fill(".new-todo", "milk")
    page.press(".new-todo", "Enter")
    page.fill(".new-todo", "bread")
    page.press(".new-todo", "Enter")
    page.fill(".new-todo", "apples")
    page.press(".new-todo", "Enter")
    page.fill(".new-todo", "bananas")
    page.press(".new-todo", "Enter")
    page.fill(".new-todo", "fish")
    page.press(".new-todo", "Enter")

    page.check("text=milkbreadapplesbananasfish >> :nth-match(input[type=\"checkbox\"], 3)")
    page.check("text=milkbreadapplesbananasfish >> :nth-match(input[type=\"checkbox\"], 5)")

    page.click("text=All Active Completed")
    page.click("text=Clear completed")
    page.click("text=All Active Completed")

    count_label = page.query_selector('.todo-count').inner_text()
    assert count_label == '3 items left'

    page.close()
    context.close()
    browser.close()


def test_todoaction():
    with sync_playwright() as playwright:
        run(playwright)
