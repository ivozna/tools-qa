from playwright.sync_api import Playwright
from autocomplete_project.autocomplete_page_object import AutoCompletePage


class SingleAutoComplete(AutoCompletePage):
    def __init__(self, playwright: Playwright):
        super().__init__(playwright)
        self.browser = playwright.chromium.launch(headless=False, slow_mo=500)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()



