from pytest import fixture
from playwright.sync_api import sync_playwright
from Example.application import App


@fixture()
def get_playwright():
    with sync_playwright() as playwright:
        yield playwright


@fixture()
def desktop_app_auth(desktop_app):
    desktop_app.goto('/login')
    desktop_app.login('alice', 'Qamania123')
    yield desktop_app

@fixture()
def desktop_app(get_playwright):
    app = App(get_playwright, base_url='http://127.0.0.1:8000')
    app.goto('/')
    yield app
    app.close()

