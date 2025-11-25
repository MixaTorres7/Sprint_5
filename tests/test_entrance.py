import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordLocators
from test_data import TestData

class TestLogin:
    
    def test_login_from_main_page(self, driver, base_url):
        driver.get(base_url)
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(TestData.EXISTING_USER["email"])
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(TestData.EXISTING_USER["password"])
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()
        WebDriverWait(driver, 15).until(
            EC.url_contains(base_url)
        )
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        assert order_button.is_displayed()

    def test_login_from_personal_account_link(self, driver, base_url):
        driver.get(base_url)
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(TestData.EXISTING_USER["email"])
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(TestData.EXISTING_USER["password"])
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()
        WebDriverWait(driver, 15).until(
            EC.url_contains(base_url)
        )
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        assert order_button.is_displayed()

    def test_login_from_registration_form(self, driver, base_url):
        driver.get(f"{base_url}/register")
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        )
        login_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(TestData.EXISTING_USER["email"])
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(TestData.EXISTING_USER["password"])
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()
        WebDriverWait(driver, 15).until(
            EC.url_contains(base_url)
        )
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        assert order_button.is_displayed()

    def test_login_from_forgot_password_form(self, driver, base_url):
        driver.get(f"{base_url}/forgot-password")
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordLocators.LOGIN_LINK)
        )
        login_link.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(TestData.EXISTING_USER["email"])
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(TestData.EXISTING_USER["password"])
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()
        WebDriverWait(driver, 15).until(
            EC.url_contains(base_url)
        )
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        assert order_button.is_displayed()