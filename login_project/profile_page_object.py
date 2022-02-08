from playwright.sync_api import Playwright

class ProfilePage:
    def __init__(self, playwright: Playwright, base_url: str, headless=False):
        self.browser = playwright.chromium.launch(headless=headless, slow_mo=500)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.base_url = base_url

        self.page.on("dialog", lambda dialog: dialog.accept())

    def goto(self, endpoint: str, use_base_url=True):
        if use_base_url:
            self.page.goto(self.base_url + endpoint)
        else:
            self.page.goto(endpoint)

    def login(self, login, password):
        self.page.fill('#userName', login)
        self.page.fill('#password', password)
        self.page.click('#login')

    def go_to_store(self):
        self.page.click('#gotoStore')

    def click_book(self, book_id):
        self.page.click(f'.rt-tr-group a[href="/books?book={book_id}"]')

    def add_book(self):
        self.page.click('.text-right >> text="Add To Your Collection"')

    def back_to_store(self):
        self.page.click('.text-left >> text="Back To Book Store"')

    def get_books(self):
        result = [i.inner_text() for i in self.page.query_selector_all('.rt-tbody a')]
        return result

    def delete_all_books(self):
        self.page.click('.text-right >> text="Delete All Books"')
        self.page.click('#closeSmallModal-ok')

    def is_profile_empty(self):
        return self.page.query_selector_all('.rt-tbody a[href^="/profile"]') == []

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
