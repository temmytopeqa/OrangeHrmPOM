import pytest
from selenium import webdriver
from ActionPage.login_page import LoginPage
from Config.configuration import Config
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@pytest.fixture(scope="module")
def driver_setup():
    driver = webdriver.Chrome()
    driver.implicitly_wait(20)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
    login_page.open_login_page(Config.BASE_URL)
    return login_page


def test_login_page_on_automation_play_ground_website(login):
    login.open_login_page(Config.BASE_URL)
    login.enter_username(Config.USERNAME)
    login.enter_password(Config.PASSWORD)
    login.click_login_button()

    # Wait for homepage element that confirms page loaded
    wait = WebDriverWait(login.driver, 15)

    # Replace below locator with an actual locator for an element only visible on homepage
    homepage_element_locator = (By.ID, "homepage-unique-element-id")

    wait.until(EC.visibility_of_element_located(homepage_element_locator))

