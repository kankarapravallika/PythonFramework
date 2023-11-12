# from selenium.webdriver.chrome import webdriver
import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from tests.BaseTest import BaseTest


# @pytest.mark.usefixtures("setup_and_teardown")
class TestSearch(BaseTest):
    # home_page = HomePage(self.driver)
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_field("HP")
        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_product()

    def test_search_for_a_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_field("Honda")
        search_page = SearchPage(self.driver)
        # self.driver.find_element(By.NAME, 'search').click()
        # self.driver.find_element(By.NAME, 'search').send_keys("Honda", Keys.ENTER)
        expected_text = "There is no product that matches the search criteria."
        assert search_page.get_invalid_status_of_product().__eq__(expected_text)

    def test_search_without_entering_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_field("")
        search_page = SearchPage(self.driver)
        expected_text = "There is no product that matches the search criteria."
        assert search_page.get_invalid_status_of_product().__eq__(expected_text)
