from playwright.sync_api import Playwright


class MenuPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, devtools=True, slow_mo=500)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        self.page.goto("https://demoqa.com/menu#")

    def hover_on(self, text):
        self.page.hover(f'#nav li >> text="{text}"')

    def is_visible(self, text):
        return self.page.is_visible(f'#nav li >> text="{text}"')

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()



