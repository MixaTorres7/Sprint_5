import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, ForgotPasswordLocators, PersonalAccountLocators
from test_data import TestData

class TestLogin:
    
    def test_login_from_main_page(self, driver, base_url):
        """Вход через кнопку «Войти в аккаунт» на главной."""
        print(f"=== Тест: Вход с главной страницы ===")
        driver.get(base_url)
        print(f"1. Открыта страница: {driver.current_url}")

        # Ждем и кликаем кнопку входа
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        print("2. Кнопка 'Войти в аккаунт' найдена")
        login_button.click()
        
        # Ждем перехода на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        print(f"3. Перешли на страницу входа: {driver.current_url}")

        # Заполняем форму входа
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        print("4. Поле email найдено")
        email_input.send_keys(TestData.EXISTING_USER["email"])

        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        print("5. Поле password найдено")
        password_input.send_keys(TestData.EXISTING_USER["password"])

        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()
        print("6. Форма отправлена")

        # Проверяем, что вошли - ждем появления кнопки "Оформить заказ" на главной
        WebDriverWait(driver, 15).until(
            EC.url_contains(base_url)
        )
        print(f"7. Вернулись на главную страницу: {driver.current_url}")
        
        # Проверяем, что есть кнопка "Оформить заказ" (признак успешного входа)
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        print("8. Кнопка 'Оформить заказ' найдена - вход успешен")
        
        assert order_button.is_displayed()

    def test_login_from_personal_account_link(self, driver, base_url):
        """Вход через ссылку «Личный кабинет» на главной."""
        print(f"=== Тест: Вход через Личный кабинет ===")
        driver.get(base_url)
        print(f"1. Открыта страница: {driver.current_url}")

        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_LINK)
        )
        print("2. Ссылка 'Личный Кабинет' найдена")
        personal_account_link.click()
        
        # Ждем перехода на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        print(f"3. Перешли на страницу входа: {driver.current_url}")

        # Заполняем форму
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        print("4. Поле email найдено")
        email_input.send_keys(TestData.EXISTING_USER["email"])

        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        print("5. Поле password найдено")
        password_input.send_keys(TestData.EXISTING_USER["password"])

        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()
        print("6. Форма отправлена")

        # Проверяем вход - ждем появления кнопки "Оформить заказ"
        WebDriverWait(driver, 15).until(
            EC.url_contains(base_url)
        )
        print(f"7. Вернулись на главную страницу: {driver.current_url}")
        
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        print("8. Кнопка 'Оформить заказ' найдена - вход успешен")
        
        assert order_button.is_displayed()

    def test_login_from_registration_form(self, driver, base_url):
        """Вход через ссылку в форме регистрации."""
        print(f"=== Тест: Вход из формы регистрации ===")
        driver.get(f"{base_url}/register")
        print(f"1. Открыта страница регистрации: {driver.current_url}")

        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        )
        print("2. Ссылка 'Войти' найдена")
        login_link.click()
        
        # Ждем перехода на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        print(f"3. Перешли на страницу входа: {driver.current_url}")

        # Заполняем форму входа
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        print("4. Поле email найдено")
        email_input.send_keys(TestData.EXISTING_USER["email"])

        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        print("5. Поле password найдено")
        password_input.send_keys(TestData.EXISTING_USER["password"])

        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()
        print("6. Форма отправлена")

        # Проверяем вход - ждем появления кнопки "Оформить заказ"
        WebDriverWait(driver, 15).until(
            EC.url_contains(base_url)
        )
        print(f"7. Вернулись на главную страницу: {driver.current_url}")
        
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        print("8. Кнопка 'Оформить заказ' найдена - вход успешен")
        
        assert order_button.is_displayed()

    def test_login_from_forgot_password_form(self, driver, base_url):
        """Вход через ссылку в форме восстановления пароля."""
        print(f"=== Тест: Вход из формы восстановления пароля ===")
        driver.get(f"{base_url}/forgot-password")
        print(f"1. Открыта страница восстановления пароля: {driver.current_url}")

        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(ForgotPasswordLocators.LOGIN_LINK)
        )
        print("2. Ссылка 'Войти' найдена")
        login_link.click()
        
        # Ждем перехода на страницу входа
        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        print(f"3. Перешли на страницу входа: {driver.current_url}")

        # Заполняем форму входа
        email_input = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        print("4. Поле email найдено")
        email_input.send_keys(TestData.EXISTING_USER["email"])

        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        print("5. Поле password найдено")
        password_input.send_keys(TestData.EXISTING_USER["password"])

        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        submit_button.click()
        print("6. Форма отправлена")

        # Проверяем вход - ждем появления кнопки "Оформить заказ"
        WebDriverWait(driver, 15).until(
            EC.url_contains(base_url)
        )
        print(f"7. Вернулись на главную страницу: {driver.current_url}")
        
        order_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Оформить заказ')]"))
        )
        print("8. Кнопка 'Оформить заказ' найдена - вход успешен")
        
        assert order_button.is_displayed()