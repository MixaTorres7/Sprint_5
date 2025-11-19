# test_stellar_burgers.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- ПЕРЕХОД В ЛИЧНЫЙ КАБИНЕТ ---

def test_navigate_to_personal_account(driver, user_credentials, base_url):
    """Переход в Личный кабинет по клику на «Личный кабинет»."""
    # Сначала логинимся
    driver.get(base_url)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )
    login_button.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
    )
    email_input.send_keys(user_credentials["email"])

    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys(user_credentials["password"])

    submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_button.click()

    # Переходим в ЛК по кнопке в шапке
    personal_account_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
    )
    personal_account_link.click()

    # Проверяем URL
    WebDriverWait(driver, 10).until(
        EC.url_contains("account/profile")
    )
    assert "profile" in driver.current_url, "Не перешли в Личный кабинет"


# --- ПЕРЕХОД ИЗ ЛК В КОНСТРУКТОР ---

def test_navigate_from_personal_account_to_constructor_by_button(driver, user_credentials, base_url):
    """Переход из ЛК в Конструктор по кнопке «Конструктор»."""
    # Логинимся
    driver.get(base_url)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )
    login_button.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
    )
    email_input.send_keys(user_credentials["email"])

    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys(user_credentials["password"])

    submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_button.click()

    # Переходим в ЛК
    personal_account_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
    )
    personal_account_link.click()

    # Переходим в Конструктор
    constructor_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Конструктор']"))
    )
    constructor_button.click()

    # Проверяем, что мы в Конструкторе
    WebDriverWait(driver, 10).until(
        EC.url_contains("constructor")
    )
    assert "constructor" in driver.current_url, "Не перешли в Конструктор из ЛК"


def test_navigate_from_personal_account_to_constructor_by_logo(driver, user_credentials, base_url):
    """Переход из ЛК в Конструктор по логотипу Stellar Burgers."""
    # Логинимся
    driver.get(base_url)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )
    login_button.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
    )
    email_input.send_keys(user_credentials["email"])

    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys(user_credentials["password"])

    submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_button.click()

    # Переходим в ЛК
    personal_account_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
    )
    personal_account_link.click()

    # Кликаем по логотипу
    logo = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//img[contains(@src, 'logo')]"))
    )
    logo.click()

    # Проверяем, что вернулись в Конструктор
    WebDriverWait(driver, 10).until(
        EC.url_contains("constructor")
    )
    assert "constructor" in driver.current_url, "Не перешли в Конструктор по логотипу"


# --- ВЫХОД ИЗ АККАУНТА ---

def test_logout_from_personal_account(driver, user_credentials, base_url):
    """Выход по кнопке «Выход» в Личном кабинете."""
    # Логинимся
    driver.get(base_url)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )
    login_button.click()

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
    )
    email_input.send_keys(user_credentials["email"])

    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys(user_credentials["password"])

    submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_button.click()

    # Переходим в ЛК
    personal_account_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
    )
    personal_account_link.click()

    # Находим кнопку «Выход»
    logout_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Выход']"))
    )
    logout_button.click()

    # Проверяем, что вышли (вернулись на главную или страницу входа)
    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )
    assert "login" in driver.current_url or "constructor" in driver.current_url, "Не вышли из аккаунта"

