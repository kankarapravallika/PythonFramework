import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest
from tests.conftest import setup_and_teardown


# @pytest.mark.usefixtures("setup_and_teardown")
class TestLogin(BaseTest):
    def test_login_with_valid_credentials(self):
        home_page = HomePage(self.driver)
        home_page.click_on_my_account_drop_menu()
        home_page.click_on_login_link()
        login_page = LoginPage(self.driver)
        login_page.enter_email("amotooricap9@gmail.com")
        login_page.enter_password("12345")
        login_page.click_login()
        assert login_page.get_invalid_login_msg().__eq__(
            'Warning: No match for E-Mail Address and/or Password.')
