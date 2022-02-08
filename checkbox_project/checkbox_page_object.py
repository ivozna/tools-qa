from playwright.sync_api import Playwright


class CheckBoxPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(ignore_https_errors=True)
        self.page = self.context.new_page()

        self.page.goto("https://demoqa.com/checkbox")

    def toggle(self, menu_item):
        self.page.click(f'button:left-of(:text("{menu_item}"))')

    def check_menu(self, menu_item):
        self.page.click(f'.rct-checkbox:left-of(:text("{menu_item}"))')

    def check_selected(self, items):
        result = self.page.query_selector('#result').inner_text()
        for item in items:
            return item in result

    def get_size(self):
        return len(self.page.query_selector_all('#result .text-success'))

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
