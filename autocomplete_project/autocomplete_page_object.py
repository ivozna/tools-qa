from playwright.sync_api import Playwright


class AutoCompletePage:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False, slow_mo=500)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        self.page.goto('https://demoqa.com/auto-complete')

    def fill_color(self, color):
        self.page.fill('#autoCompleteMultipleInput', color)
        self.page.click(f'.auto-complete__menu >> text={color}')

    def type_color(self, color):
        self.page.fill('#autoCompleteMultipleInput', color)

    def get_options(self):
        options = [option.inner_text() for option in self.page.query_selector_all('.auto-complete__option')]
        return options

    def click_outside(self):
        self.page.click('.col-12')

    def delete_color(self, color):
        self.page.click(f'.auto-complete__multi-value__remove:right-of(:text("{color}"))')

    def get_results(self):
        colors = [color.inner_text() for color in self.page.query_selector_all('.css-12jo7m5')]
        return colors

    def delete_all_colors(self):
        self.page.click('.auto-complete__clear-indicator')

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()



