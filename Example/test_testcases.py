def test_new_testcase(desktop_app_auth):
    desktop_app_auth.goto('/test/new')
    desktop_app_auth.create_test('hello', 'world')
    desktop_app_auth.goto('/tests/')
    assert desktop_app_auth.test_cases.check_test_exists('hello')
    desktop_app_auth.test_cases.delete_test_by_name('hello')


def test_new_testcase_no_descr(desktop_app_auth):
    desktop_app_auth.goto('/test/new')
    desktop_app_auth.create_test('hello', '')
    desktop_app_auth.goto('/tests/')
    assert desktop_app_auth.test_cases.check_test_exists('hello')
    desktop_app_auth.test_cases.delete_test_by_name('hello')


def test_new_testcase_digits_name(desktop_app_auth):
    desktop_app_auth.goto('/test/new')
    desktop_app_auth.create_test('123', 'world')
    desktop_app_auth.goto('/tests/')
    assert desktop_app_auth.test_cases.check_test_exists('123')
    desktop_app_auth.test_cases.delete_test_by_name('123')

# from playwright.sync_api import Playwright, sync_playwright
#
#
# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False, devtools=True)
#     context = browser.new_context()
#     page = context.new_page()
#
#     page.goto("http://127.0.0.1:8000/login/?next=/")
#
#     page.fill("input[name=\"username\"]", "alice")
#     page.fill("input[name=\"password\"]", "Qamania123")
#     page.click("text=Login")
#
#     page.click("text=Create new test")
#     page.fill("input[name=\"name\"]", "hello")
#     page.fill("textarea[name=\"description\"]", "world")
#     page.click("input:has-text(\"Create\")")
#
#     page.click("text=Test Cases")
#     assert page.query_selector('//td[text()="hello"]') is not None
#
#     page.click('.deleteBtn:right-of(:text("world"))')
#
#     page.close()
#     context.close()
#     browser.close()
#
#
# def test_test2():
#     with sync_playwright() as playwright:
#         run(playwright)
