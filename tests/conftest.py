import pytest
from selenium import webdriver
from test_data import TestData

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def base_url():
    return "https://stellarburgers.education-services.ru"

@pytest.fixture
def user_credentials():
    return TestData.EXISTING_USER