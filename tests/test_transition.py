import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators, LoginPageLocators, PersonalAccountLocators
from test_data import TestData

class TestNavigation:
    
    @pytest.fixture
    def login_user(self, driver, base_url):
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

    def test_navigate_to_personal_account(self, login_user, base_url):
        driver = login_user
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )
        assert "account" in driver.current_url

    def test_navigate_from_personal_account_to_constructor_by_button(self, login_user, base_url):
        driver = login_user
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )
        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        assert base_url in driver.current_url

    def test_navigate_from_personal_account_to_constructor_by_logo(self, login_user, base_url):
        driver = login_user
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )
        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        )
        logo.click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        assert base_url in driver.current_url

    def test_logout_from_personal_account(self, login_user, base_url):
        driver = login_user
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        )
        logout_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        assert "login" in driver.current_url