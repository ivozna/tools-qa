from pytest import fixture
from playwright.sync_api import sync_playwright
from updown_project.updown_page_object import Updown_page


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def updown_page(get_playwright):
    page = Updown_page(get_playwright)
    yield page
    page.close()
