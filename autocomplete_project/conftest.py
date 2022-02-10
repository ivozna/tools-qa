from pytest import fixture
from playwright.sync_api import sync_playwright
from autocomplete_project.autocomplete_page_object import AutoCompletePage
from autocomplete_project.single_autocom_page_object import SingleAutoComplete


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def autocomplete_page(get_playwright):
    page = AutoCompletePage(get_playwright)
    yield page
    page.close()



