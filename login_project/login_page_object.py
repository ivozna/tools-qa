from playwright.sync_api import Playwright


class LoginPage:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless, slow_mo=500)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def fill_info(self, selector, info):
        self.page.fill(selector, info)

    def login(self):
        self.page.click('#login')

    def invalid_result(self):
        return self.page.inner_text('#output')

    def is_empty(self, selector):
        return self.page.input_value(selector) == ''

    def valid_result(self):
        return self.page.inner_text("#userName-value")

    def click_captcha(self):
        self.page.click('#g-recaptcha')

    def register(self, callback):
        self.page.on('dialog', callback)
        self.page.click('#register')

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
