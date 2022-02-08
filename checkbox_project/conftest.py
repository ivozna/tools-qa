from pytest import fixture
from playwright.sync_api import sync_playwright
from checkbox_project.checkbox_page_object import CheckBoxPage


@fixture
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright



@fixture()
def checkbox_page(get_playwright):
    app = CheckBoxPage(get_playwright)
    yield app
    app.close()



