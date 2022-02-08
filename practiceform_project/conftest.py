from pytest import fixture
from playwright.sync_api import sync_playwright
from practiceform_page_object import PracticeFormPage


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def practice_form(get_playwright):
    page = PracticeFormPage(get_playwright)
    yield page
    page.close()
