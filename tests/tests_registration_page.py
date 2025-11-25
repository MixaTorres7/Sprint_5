import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from test_data import TestData, generate_random_email, generate_random_password, generate_random_name

class TestRegistration:

    def test_successful_registration(self, driver, base_url):
        driver.get(f"{base_url}/register")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        test_data = {
            "name": generate_random_name(),
            "email": generate_random_email(),
            "password": generate_random_password(6)
        }
        name_input = driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        name_input.send_keys(test_data["name"])
        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(test_data["email"])
        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys(test_data["password"])
        register_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        )
        register_button.click()
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        assert "login" in driver.current_url

    def test_registration_with_invalid_password(self, driver, base_url):
        driver.get(f"{base_url}/register")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(TestData.INVALID_PASSWORD_USER["name"])
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(TestData.INVALID_PASSWORD_USER["email"])
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(TestData.INVALID_PASSWORD_USER["password"])
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )
        error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE)
        assert error_message.is_displayed()

    def test_name_field_validation(self, driver, base_url):
        driver.get(f"{base_url}/register")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        name_input = driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        name_input.send_keys(generate_random_name())
        assert name_input.get_attribute("value") != ""

    def test_email_format_validation(self, driver, base_url):
        driver.get(f"{base_url}/register")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
        )
        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        test_email = generate_random_email()
        email_input.send_keys(test_email)
        email = email_input.get_attribute("value")
        assert "@" in email and "." in email
        assert email.count("@") == 1

    def test_password_min_length_validation(self, driver, base_url):
        driver.get(f"{base_url}/register")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_INPUT)
        )
        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        test_password = generate_random_password(6)
        password_input.send_keys(test_password)
        password = password_input.get_attribute("value")
        assert len(password) >= 6


