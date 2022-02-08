from playwright.sync_api import Playwright


class Slider:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        self.page.goto('https://demoqa.com/slider')

    def move_to(self, value):
        box = self.page.query_selector('.range-slider').bounding_box()
        current_range = self.get_range_val()

        self.page.mouse.move(box['x'], box['y'])
        self.page.mouse.down()

        initial_x = box['x'] + (int(current_range) * box['width'] / 100)
        i = 0
        while int(self.get_range_val()) != value:
            self.page.mouse.move(initial_x + i, box['y'])

            if value < int(current_range):
                i = i - 1
            else:
                i = i + 1

        self.page.mouse.up()

    def get_location(self):
        return self.page.input_value('#sliderValue')

    def get_range_val(self):
        return self.page.input_value('.range-slider')

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()

# page.waitForSelector('#browsers', state='visible', timeout=30000)
