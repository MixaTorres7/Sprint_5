import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from locators import MainPageLocators

class TestConstructor:
    
    @pytest.mark.parametrize("tab_locator,header_locator,expected_text", [
        (MainPageLocators.BUNS_TAB, MainPageLocators.BUNS_HEADER, "Булки"),
        (MainPageLocators.SAUCES_TAB, MainPageLocators.SAUCES_HEADER, "Соусы"),
        (MainPageLocators.FILLINGS_TAB, MainPageLocators.FILLINGS_HEADER, "Начинки")
    ])
    def test_navigate_to_section(self, driver, base_url, tab_locator, header_locator, expected_text):
        """Параметризованный тест переходов между разделами конструктора."""
        driver.get(base_url)

        # Отладочная информация
        print(f"Текущий URL: {driver.current_url}")
        print(f"Заголовок страницы: {driver.title}")

        # Ждём загрузки конструктора
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(MainPageLocators.BUNS_TAB)
        )

        # Кликаем на указанную вкладку с помощью JavaScript
        tab = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(tab_locator)
        )
        
        # Способ 1: Используем JavaScript для клика (обходит проблему перекрытия)
        driver.execute_script("arguments[0].click();", tab)
        
        # ИЛИ Способ 2: Используем ActionChains для более точного клика
        # actions = ActionChains(driver)
        # actions.move_to_element(tab).click().perform()

        # Ждём появления заголовка раздела
        WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(header_locator)
        )

        # Проверяем, что заголовок соответствует ожидаемому
        header = driver.find_element(*header_locator)
        assert header.text == expected_text, f"Ожидался раздел '{expected_text}', но найден '{header.text}'"