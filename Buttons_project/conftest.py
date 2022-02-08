from pytest import fixture
from playwright.sync_api import sync_playwright
from buttons_page_object import ButtonsPage


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def buttons(get_playwright):
    page = ButtonsPage(get_playwright)
    yield page
    page.close()
