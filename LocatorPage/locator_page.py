from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.CSS_SELECTOR, "input[name='username']")
    PASSWORD = (By.CSS_SELECTOR, "Input[name='password']")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")