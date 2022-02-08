from pytest import fixture
from playwright.sync_api import sync_playwright
from datepicker_project.datepicker_page_object import Datapicker_page
from datepicker_project.dateandtime_page_object import Dateandtime_page

@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def datepicker_page(get_playwright):
    page = Datapicker_page(get_playwright)
    yield page
    page.close()

@fixture()
def dateandtime_page(get_playwright):
    page = Dateandtime_page(get_playwright)
    yield page
    page.close()

