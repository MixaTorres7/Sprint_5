import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators, LoginPageLocators
from test_data import TestData

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://stellarburgers.education-services.ru"

@pytest.fixture
def user_credentials():
    return TestData.EXISTING_USER

@pytest.fixture
def login_user(driver, base_url):
    driver.get(base_url)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
    )
    login_button.click()
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    email_input.send_keys(TestData.EXISTING_USER["email"])
    password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    password_input.send_keys(TestData.EXISTING_USER["password"])
    submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
    submit_button.click()
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
    )
    return driver