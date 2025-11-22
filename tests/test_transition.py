import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators, LoginPageLocators, PersonalAccountLocators
from test_data import TestData

class TestNavigation:
    
    @pytest.fixture
    def login_user(self, driver, base_url):
        """Фикстура для логина пользователя"""
        driver.get(base_url)
        print("=== Фикстура: Логин пользователя ===")
        
        # Ждем и кликаем кнопку входа
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        login_button.click()

        # Заполняем форму входа
        email_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        email_input.send_keys(TestData.EXISTING_USER["email"])

        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_input.send_keys(TestData.EXISTING_USER["password"])

        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()
        
        # Ждем завершения входа - проверяем появление кнопки "Оформить заказ"
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        print("Логин выполнен успешно")
        return driver

    def test_navigate_to_personal_account(self, login_user, base_url):
        """Переход в Личный кабинет по клику на «Личный кабинет»."""
        driver = login_user
        print("=== Тест: Переход в Личный кабинет ===")
        
        # Переходим в ЛК по кнопке в шапке
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_link.click()

        # Проверяем URL
        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )
        print(f"Текущий URL: {driver.current_url}")
        assert "account" in driver.current_url, "Не перешли в Личный кабинет"

    def test_navigate_from_personal_account_to_constructor_by_button(self, login_user, base_url):
        """Переход из ЛК в Конструктор по кнопке «Конструктор»."""
        driver = login_user
        print("=== Тест: Переход из ЛК в Конструктор по кнопке ===")
        
        # Переходим в ЛК
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_link.click()

        # Ждем загрузки ЛК
        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )

        # Переходим в Конструктор
        constructor_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_button.click()

        # Проверяем, что мы в Конструкторе (по кнопке "Оформить заказ")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        print(f"Текущий URL: {driver.current_url}")
        assert base_url in driver.current_url, "Не перешли в Конструктор из ЛК"

    def test_navigate_from_personal_account_to_constructor_by_logo(self, login_user, base_url):
        """Переход из ЛК в Конструктор по логотипу Stellar Burgers."""
        driver = login_user
        print("=== Тест: Переход из ЛК в Конструктор по логотипу ===")
        
        # Переходим в ЛК
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_link.click()

        # Ждем загрузки ЛК
        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )

        # Кликаем по логотипу
        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        )
        logo.click()

        # Проверяем, что вернулись в Конструктор (по кнопке "Оформить заказ")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        print(f"Текущий URL: {driver.current_url}")
        assert base_url in driver.current_url, "Не перешли в Конструктор по логотипу"

    def test_logout_from_personal_account(self, login_user, base_url):
        """Выход по кнопке «Выход» в Личном кабинете."""
        driver = login_user
        print("=== Тест: Выход из аккаунта ===")
        
        # Переходим в ЛК
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        personal_account_link.click()

        # Ждем загрузки ЛК
        WebDriverWait(driver, 10).until(
            EC.url_contains("account")
        )

        # Находим кнопку «Выход»
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        )
        logout_button.click()

        # Проверяем, что вышли (вернулись на страницу входа)
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        print(f"Текущий URL: {driver.current_url}")
        assert "login" in driver.current_url, "Не вышли из аккаунта"