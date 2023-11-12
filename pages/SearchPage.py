from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver

    valid_hp_product_link_text = "HP LP3065"
    invalid_product_text = "//input[@id='button-search']//following-sibling::p"

    def display_status_of_product(self):
        return self.driver.find_element(By.LINK_TEXT, self.valid_hp_product_link_text).is_displayed()

    def get_invalid_status_of_product(self):
        return self.driver.find_element(By.XPATH, self.invalid_product_text).text
