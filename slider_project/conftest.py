from pytest import fixture
from playwright.sync_api import sync_playwright
from slider_project.slider_page_object import Slider


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def slider_page(get_playwright):
    page = Slider(get_playwright)
    yield page
    page.close()
