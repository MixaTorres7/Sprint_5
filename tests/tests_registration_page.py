# test_stellar_burgers.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- РЕГИСТРАЦИЯ ---

def test_successful_registration(driver, user_credentials, base_url):
    """Успешная регистрация: имя не пустое, email валиден, пароль >=6 символов."""
    driver.get(f"{base_url}/register")

    # Заполняем поля
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[label[text()='Имя']]/input"))
    )
    name_input.send_keys(user_credentials["name"])

    email_input = driver.find_element(By.XPATH, "//div[label[text()='Email']]/input")
    email_input.send_keys(user_credentials["email"])

    password_input = driver.find_element(By.XPATH, "//div[label[text()='Пароль']]/input")
    password_input.send_keys(user_credentials["password"])

    # Нажимаем кнопку
    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()

    # Ждём перенаправления на страницу входа
    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )

    assert "login" in driver.current_url, "Не произошло перенаправление после регистрации"


def test_name_field_not_empty(driver, user_credentials, base_url):
    """Поле «Имя» должно быть не пустым."""
    driver.get(f"{base_url}/register")
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[label[text()='Имя']]/input"))
    )
    name_input.send_keys(user_credentials["name"])
    assert name_input.get_attribute("value") != "", "Поле 'Имя' пустое"


def test_email_format_valid(driver, user_credentials, base_url):
    """Email должен быть в формате логин@домен."""
    driver.get(f"{base_url}/register")
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[label[text()='Email']]/input"))
    )
    email_input.send_keys(user_credentials["email"])
    email = email_input.get_attribute("value")
    assert "@" in email and "." in email, "Email не содержит '@' или '.'"
    assert email.count("@") == 1, "Email содержит более одного '@'"


def test_password_min_length(driver, user_credentials, base_url):
    """Пароль должен быть не менее 6 символов."""
    driver.get(f"{base_url}/register")
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[label[text()='Пароль']]/input"))
    )
    password_input.send_keys(user_credentials["password"])
    password = password_input.get_attribute("value")
    assert len(password) >= 6, f"Пароль короче 6 символов: {len(password)}"





