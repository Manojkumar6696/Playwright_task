# TestScripts/test_login.py

import pytest
from playwright.sync_api import expect
from Page_Object.login_page import LoginPage
from Test_Data.data import Data

# setup and teardown
@pytest.fixture(scope="function")
def login_page():
    # setup
    page = LoginPage()
    yield page
    # teardown
    page.close()


class TestGuviLogin:
    def test_valid_login(self, login_page):
        # navigate to login page
        login_page.navigate()

        # perform login with valid credentials
        login_page.login(Data.username, Data.password)

        # assertion - check if dashboard is visible
        expect(login_page.page).to_have_url(Data.dashboard_url)
        print("SUCCESS: Guvi_page Logged in!")

    def test_invalid_login(self, login_page):
        # navigate to login page
        login_page.navigate()

        # perform login with invalid credentials
        login_page.login(Data.invalid_username, Data.invalid_password)

        # assertion
        expect(login_page.page).not_to_have_url(Data.dashboard_url)
        print("SUCCESS: Not Logged in!")