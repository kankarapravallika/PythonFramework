from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    search_box_field_name = "search"
    my_account_drop_menu = "//span[text()='My Account']"
    login_link = "Login"

    def enter_product_into_search_field(self, product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(product_name, Keys.ENTER)

    def click_on_my_account_drop_menu(self):
        self.driver.find_element(By.XPATH, self.my_account_drop_menu).click()

    def click_on_login_link(self):
        self.driver.find_element(By.LINK_TEXT, self.login_link).click()