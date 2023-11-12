from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    input_email = "input-email"
    input_password = "input-password"
    login_button = "//input[@value='Login']"
    invalid_login_alert = "//div[contains(@class,'alert-danger')]"

    def enter_email(self, email):
        self.driver.find_element(By.ID, self.input_email).send_keys(email)

    def enter_password(self, pwd):
        self.driver.find_element(By.ID, self.input_password).send_keys(pwd)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button).click()

    def get_invalid_login_msg(self):
        return self.driver.find_element(By.XPATH, self.invalid_login_alert).text
