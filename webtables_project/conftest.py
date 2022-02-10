from pytest import fixture
from playwright.sync_api import sync_playwright
from webtables_project.webtables_page_object import WebTablesPage


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def web_tables_page(get_playwright):
    app = WebTablesPage(get_playwright)
    yield app
    app.close()

