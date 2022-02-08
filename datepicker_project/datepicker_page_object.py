from playwright.sync_api import Playwright


class DataPickerPage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, slow_mo=1000)
        self.context = self.browser.new_context(ignore_https_errors=True)
        self.page = self.context.new_page()

        self.page.goto("https://demoqa.com/date-picker")
        self.page.click("#datePickerMonthYearInput")

    def select_month(self, month):
        self.page.select_option('.react-datepicker__month-select', label=month)

    def select_month_next(self):
        self.page.click('.react-datepicker__navigation--next')

    def select_month_previous(self):
        self.page.click('.react-datepicker__navigation--previous')

    def select_year(self, year):
        self.page.select_option(".react-datepicker__year-select", label=year)

    def select_day(self, day):
        self.page.click(f'.react-datepicker__day >> text={day}')

    def get_date(self):
        return self.page.input_value("#datePickerMonthYearInput")

    def get_current_month(self):
        return self.page.inner_text(".react-datepicker__current-month")

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()


