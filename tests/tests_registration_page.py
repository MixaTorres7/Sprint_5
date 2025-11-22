import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators
from test_data import TestData

class TestRegistration:

    def test_successful_registration(self, driver, base_url):
        """Успешная регистрация с валидными данными"""
        print("=== Тест успешной регистрации ===")
        driver.get(f"{base_url}/register")
        print(f"Открыта страница: {driver.current_url}")

        # Ждем загрузки формы
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        print("✓ Форма регистрации загружена")

        # Используем реальные данные пользователя
        test_data = {
            "name": TestData.VALID_USER["name"],
            "email": TestData.VALID_USER["email"],
            "password": TestData.VALID_USER["password"]
        }

        print(f"Данные для регистрации: {test_data}")

        # Заполняем форму с проверками
        name_input = driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        name_input.send_keys(test_data["name"])
        print(f"✓ Введено имя: {test_data['name']}")

        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(test_data["email"])
        print(f"✓ Введен email: {test_data['email']}")

        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys(test_data["password"])
        print("✓ Введен пароль")

        # Проверяем что кнопка существует и кликабельна
        register_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable(RegistrationPageLocators.REGISTER_BUTTON)
        )
        print("✓ Кнопка 'Зарегистрироваться' найдена и кликабельна")

        # Делаем скриншот перед кликом
        driver.save_screenshot("before_registration.png")
        print("✓ Скриншот сохранен: before_registration.png")

        # Нажимаем кнопку регистрации
        register_button.click()
        print("✓ Кнопка регистрации нажата")

        # Проверяем редирект на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        print(f"✓ Произошел редирект на: {driver.current_url}")
        
        assert "login" in driver.current_url, "Не произошло перенаправление после регистрации"

    def test_registration_with_invalid_password(self, driver, base_url):
        """Ошибка при регистрации с некорректным паролем (<6 символов)"""
        driver.get(f"{base_url}/register")

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        
        # Заполняем форму с коротким паролем
        driver.find_element(*RegistrationPageLocators.NAME_INPUT).send_keys(TestData.INVALID_PASSWORD_USER["name"])
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(TestData.INVALID_PASSWORD_USER["email"])
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(TestData.INVALID_PASSWORD_USER["password"])
        
        # Нажимаем кнопку регистрации
        driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON).click()
        
        # Проверяем, что остались на странице регистрации и есть сообщение об ошибке
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
        )
        
        error_message = driver.find_element(*RegistrationPageLocators.ERROR_MESSAGE)
        assert error_message.is_displayed(), "Сообщение об ошибке не отображается"

    def test_name_field_validation(self, driver, base_url):
        """Проверка, что поле 'Имя' не пустое"""
        driver.get(f"{base_url}/register")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        
        name_input = driver.find_element(*RegistrationPageLocators.NAME_INPUT)
        name_input.send_keys(TestData.VALID_USER["name"])
        assert name_input.get_attribute("value") != "", "Поле 'Имя' пустое"

    def test_email_format_validation(self, driver, base_url):
        """Проверка формата email"""
        driver.get(f"{base_url}/register")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.EMAIL_INPUT)
        )
        
        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        email_input.send_keys(TestData.VALID_USER["email"])
        email = email_input.get_attribute("value")
        assert "@" in email and "." in email, "Email не содержит '@' или '.'"
        assert email.count("@") == 1, "Email содержит более одного '@'"

    def test_password_min_length_validation(self, driver, base_url):
        """Проверка минимальной длины пароля"""
        driver.get(f"{base_url}/register")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(RegistrationPageLocators.PASSWORD_INPUT)
        )
        
        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)
        password_input.send_keys(TestData.VALID_USER["password"])
        password = password_input.get_attribute("value")
        assert len(password) >= 6, f"Пароль короче 6 символов: {len(password)}"



