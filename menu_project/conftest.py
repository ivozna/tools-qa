from pytest import fixture
from playwright.sync_api import sync_playwright
from menu_project.menu_page_object import MenuPage


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def menu_page(get_playwright):
    page = MenuPage(get_playwright)
    yield page
    page.close()