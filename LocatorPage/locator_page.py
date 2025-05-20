from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    SUBMIT = (By.ID, "login-button")
    DASHBOARD_HEADER = (By.XPATH, "//header//div[1]/div[1]")  # Adjust name for clarity