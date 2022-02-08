from pytest import fixture
from playwright.sync_api import sync_playwright
from textbox_project.textbox_page_object import TextBoxPage


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def textbox_page(get_playwright):
    app = TextBoxPage(get_playwright)
    yield app
    app.close()
