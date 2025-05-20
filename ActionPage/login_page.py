from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from LocatorPage.locator_page import LoginLocators

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_login_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        username_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "username"))
        )
        username_field.send_keys(username)

    def enter_password(self, password):
        password_field = self.wait.until(
            EC.visibility_of_element_located((By.NAME, "password"))
        )
        password_field.send_keys(password)

    def click_login_button(self):
        login_button = self.wait.until(
            EC.element_to_be_clickable((By.TAG_NAME, "button"))
        )
        login_button.click()
