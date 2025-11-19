# conftest.py
from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def driver():
    """Фикстура для запуска и закрытия браузера."""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="session")
def user_credentials():
    
    """Учётные данные пользователя"""
    
    return {
        "name": "Роман",
        "email": "mixavolkov34111@yandex.ru",
        "password": "123456"
    }

@pytest.fixture(scope="session")
def base_url():
    return "https://stellarburgers.education-services.ru"