from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# --- ВХОД ---

def test_login_from_main_page(driver, user_credentials, base_url):
    """Вход через кнопку «Войти в аккаунт» на главной."""
    driver.get(base_url)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']"))
    )
    login_button.click()

    # Заполняем форму входа
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
    )
    email_input.send_keys(user_credentials["email"])

    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys(user_credentials["password"])

    submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_button.click()

    # Проверяем, что вошли (переход на ЛК)
    WebDriverWait(driver, 10).until(
        EC.url_contains("account/profile")
    )
    assert "profile" in driver.current_url, "Не удалось войти через главную"


def test_login_from_personal_account_link(driver, user_credentials, base_url):
    """Вход через ссылку «Личный кабинет» на главной."""
    driver.get(base_url)
    personal_account_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//p[text()='Личный Кабинет']"))
    )
    personal_account_link.click()

    # Заполняем форму
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
    )
    email_input.send_keys(user_credentials["email"])

    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys(user_credentials["password"])

    submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_button.click()

    # Проверяем вход
    WebDriverWait(driver, 10).until(
        EC.url_contains("account/profile")
    )
    assert "profile" in driver.current_url, "Не удалось войти через ЛК"


def test_login_from_registration_form(driver, user_credentials, base_url):
    """Вход через ссылку в форме регистрации."""
    driver.get(f"{base_url}/register")
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Зарегистрироваться']"))
    )
    login_link.click()

    # Заполняем форму входа
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
    )
    email_input.send_keys(user_credentials["email"])

    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys(user_credentials["password"])

    submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_button.click()

    # Проверяем вход
    WebDriverWait(driver, 10).until(
        EC.url_contains("account/profile")
    )
    assert "profile" in driver.current_url, "Не удалось войти из формы регистрации"


def test_login_from_forgot_password_form(driver, user_credentials, base_url):
    """Вход через ссылку в форме восстановления пароля."""
    driver.get(f"{base_url}/forgot-password")
    login_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[text()='Восстановить пароль']"))
    )
    login_link.click()

    # Заполняем форму входа
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@name='email']"))
    )
    email_input.send_keys(user_credentials["email"])

    password_input = driver.find_element(By.XPATH, "//input[@name='password']")
    password_input.send_keys(user_credentials["password"])

    submit_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    submit_button.click()

    # Проверяем вход
    WebDriverWait(driver, 10).until(
        EC.url_contains("account/profile")
    )
    assert "profile" in driver.current_url, "Не удалось войти из формы восстановления пароля"


