from playwright.sync_api import Playwright

class TextBoxPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(ignore_https_errors=True)
        self.page = self.context.new_page()
        self.page.goto("https://demoqa.com/text-box")

    def fill_name(self, name):
        self.page.fill("#userName", name)

    def fill_email(self, email):
        self.page.fill("#userEmail", email)

    def fill_current_address(self, address):
        self.page.fill("#currentAddress", address)

    def fill_permanent_address(self, address):
        self.page.fill("#permanentAddress", address)

    def submit(self):
        self.page.click("#submit")

    def get_info(self, selector):
        data = self.page.query_selector(f"#output {selector}")
        if data is not None:
            return data.inner_text()
        return None

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
