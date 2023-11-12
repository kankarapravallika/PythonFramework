import random
import string
import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from tests.BaseTest import BaseTest


# @pytest.mark.usefixtures("setup_and_teardown")
class TestRegister(BaseTest):
    def test_login_with_valid_credentials(self):
        # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        # driver.maximize_window()
        # driver.get("https://tutorialsninja.com/demo/")
        self.driver.find_element(By.XPATH, '//span[text()="My Account"]').click()
        self.driver.find_element(By.LINK_TEXT, 'Register').click()
        self.driver.find_element(By.ID, "input-firstname").send_keys(random_value("string", 7))
        self.driver.find_element(By.ID, "input-lastname").send_keys(random_value("string", 7))
        self.driver.find_element(By.ID, "input-email").send_keys(random_value("string", 7) + "@gmail.com")
        self.driver.find_element(By.ID, "input-telephone").send_keys(random_value("number", 10))
        self.driver.find_element(By.ID, "input-password").send_keys("pravalli")
        self.driver.find_element(By.ID, "input-confirm").send_keys("pravalli")
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        assert self.driver.find_element(By.XPATH, "//div[@id='content']//h1").text.__eq__(
            "Your Account Has Been Created!")
        time.sleep(5)


def random_value(type, length):
    if not isinstance(length, int) or length <= 0:
        raise ValueError("Length must be a positive integer greater than 0")
    if type == "string":
        characters = string.ascii_lowercase
        random_value = ''.join(random.choice(characters) for _ in range(length))
    elif type == "number":
        start_range = 10 ** (length - 1)
        end_range = (10 ** length) - 1
        random_value = random.randrange(start_range, end_range + 1)
    elif type == "combination":
        characters = string.ascii_lowercase + string.digits
        random_value = ''.join(random.choice(characters) for _ in range(length))
    return random_value
