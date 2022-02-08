from pytest import fixture
from playwright.sync_api import sync_playwright
from droppable_project.droppable_page_object import Simple


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def simple_page(get_playwright):
    page = Simple(get_playwright)
    yield page
    page.close()