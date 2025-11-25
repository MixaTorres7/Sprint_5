import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators

class TestConstructor:
    
    @pytest.mark.parametrize("tab_locator,header_locator,expected_text", [
        (MainPageLocators.BUNS_TAB, MainPageLocators.BUNS_HEADER, "Булки"),
        (MainPageLocators.SAUCES_TAB, MainPageLocators.SAUCES_HEADER, "Соусы"),
        (MainPageLocators.FILLINGS_TAB, MainPageLocators.FILLINGS_HEADER, "Начинки")
    ])
    def test_navigate_to_section(self, driver, base_url, tab_locator, header_locator, expected_text):
        driver.get(base_url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.BUNS_TAB)
        )
        tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(tab_locator)
        )
        driver.execute_script("arguments[0].click();", tab)
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(header_locator)
        )
        header = driver.find_element(*header_locator)
        assert header.text == expected_text