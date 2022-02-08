from playwright.sync_api import Playwright

class ButtonsPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(ignore_https_errors=True)
        self.page = self.context.new_page()

        self.page.goto('https://demoqa.com/buttons')

    def double_click(self):
        self.page.dblclick('#doubleClickBtn')

    def click(self, selector):
        self.page.click(selector)

    def right_click(self):
        self.page.click('#rightClickBtn', button='right')

    def check_result(self, selector):
        node = self.page.query_selector(f'{selector}')
        if node is not None:
            return node.inner_text()
        return None

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
