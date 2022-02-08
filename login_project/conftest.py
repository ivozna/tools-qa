from pytest import fixture
from playwright.sync_api import sync_playwright
from login_project.login_page_object import LoginPage
from login_project.profile_page_object import ProfilePage


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def login_page(get_playwright):
    page = LoginPage(get_playwright, base_url='https://demoqa.com')
    page.goto('/login')
    yield page
    page.close()


@fixture()
def register_page(get_playwright):
    page = LoginPage(get_playwright, base_url='https://demoqa.com')
    page.goto('/')
    yield page
    page.close()


@fixture()
def profile_page(get_playwright):
    page = ProfilePage(get_playwright, base_url='https://demoqa.com')
    yield page
    page.close()


@fixture()
def profile_page_auth(profile_page):
    profile_page.goto('/login')
    profile_page.login('ivozna', "Kozakoza123#")
    yield profile_page
