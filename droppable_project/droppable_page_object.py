from playwright.sync_api import Playwright, Mouse


class Simple:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()

        self.page.goto('https://demoqa.com/droppable')

    def move_to(self):
        src_box = self.page.query_selector('#draggable').bounding_box()
        tgt_box = self.page.query_selector('#droppable').bounding_box()
        mouse = self.page.mouse
        mouse.move(src_box['x'] + src_box['width'] / 2, src_box['y'] + src_box['height'] / 2)
        self.page.mouse.down()
        mouse.move(tgt_box['x'] + tgt_box['width'] / 2, tgt_box['y'] + tgt_box['height'] / 2, steps=10)
        self.page.mouse.up()

    def get_text(self):
        return self.page.inner_text('#droppable')


    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
