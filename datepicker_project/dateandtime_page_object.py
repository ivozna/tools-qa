from playwright.sync_api import Playwright
from datetime import datetime


class DateAndTimePickerPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        self.context = self.browser.new_context(ignore_https_errors=True)
        self.page = self.context.new_page()

        self.page.goto("https://demoqa.com/date-picker")
        self.page.click("#dateAndTimePickerInput")

    def select_month(self, month):
        self.page.click('.react-datepicker__month-dropdown-container')

        self.page.click(f'.react-datepicker__month-option >> text={month}')

    def select_month_next(self):
        self.page.click('.react-datepicker__navigation--next--with-time')

    def select_month_previous(self):
        self.page.click('.react-datepicker__navigation--previous')

    def select_year(self, year):
        self.page.click('.react-datepicker__year-read-view')
        current_year = datetime.today().year
        if year < current_year - 5:
            num_clicks = current_year - 5 - year
            self.page.click('.react-datepicker__navigation--years-previous', click_count=num_clicks)
        if year > current_year + 5:
            num_clicks = year - (current_year + 5)
            self.page.click('.react-datepicker__navigation--years-upcoming', click_count=num_clicks)

        self.page.click(f".react-datepicker__year-option >> text={year}")

    def select_time(self, time):
        self.page.click(f".react-datepicker__time-list-item >> text={time}")

    def select_day(self, day):
        self.page.click(f'.react-datepicker__day >> text={day}')

    def get_dateandtime(self):
        return self.page.input_value("#dateAndTimePickerInput")

    def get_current_month(self):
        return self.page.inner_text(".react-datepicker__current-month")

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
