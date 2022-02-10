from playwright.sync_api import Playwright


class WebTablesPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(ignore_https_errors=True)
        self.page = self.context.new_page()
        self.page.goto("https://demoqa.com/webtables")

    def add_user(self, form):
        self.page.click("#addNewRecordButton")
        self.page.fill("#firstName", form['name'])
        self.page.fill("#lastName", form['last_name'])
        self.page.fill("#userEmail", form['email'])
        self.page.fill("#age", form['age'])
        self.page.fill("#salary", form['salary'])
        self.page.fill("#department", form['department'])
        self.page.click("#submit")

    def check_new_record(self, user_info):
        return self.page.query_selector(f".rt-tbody >> text={user_info}")

    def fill_search(self, user_info):
        self.page.fill("#searchBox", user_info)

    def check_search_result(self, user_info):
        data = self.page.query_selector(f".rt-tbody >> text={user_info}")
        return data is not None

    def delete_record(self, user_info):
        self.page.click(f'[id^=delete-record]:right-of(:text("{user_info}"))')

    def check_delete_record(self, user_info):
        return self.page.query_selector(f".rt-tbody >> text={user_info}") is None

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()


