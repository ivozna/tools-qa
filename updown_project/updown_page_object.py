from playwright.sync_api import Playwright


class Updown_page:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context(ignore_https_errors=True)
        self.page = self.context.new_page()
        self.page.goto("https://demoqa.com/upload-download")

    def download(self):
        with self.page.expect_download() as download_info:
            self.page.click("#downloadButton")
        download = download_info.value
        filename = download.suggested_filename
        return filename

    def upload(self, path):
        with self.page.expect_file_chooser() as fc_info:
            self.page.click("#uploadFile")
        file_chooser = fc_info.value
        file_chooser.set_files(path)

    def get_path(self):
        return self.page.inner_text('#uploadedFilePath')

    def close(self):
        self.page.close()
        self.context.close()
        self.browser.close()
