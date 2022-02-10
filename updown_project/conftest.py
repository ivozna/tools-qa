from pytest import fixture
from playwright.sync_api import sync_playwright
from updown_project.updown_page_object import UpDownPage


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def updown_page(get_playwright):
    page = UpDownPage(get_playwright)
    yield page
    page.close()
