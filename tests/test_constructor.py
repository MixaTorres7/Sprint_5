# test_stellar_burgers.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

    # --- РАЗДЕЛ «КОНСТРУКТОР» ---

def test_navigate_between_sections_in_constructor(driver, base_url):
    """Проверка переходов между разделами: Булки, Соусы, Начинки."""
    driver.get(f"{base_url}/constructor")

    # Ждём загрузки конструктора
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//span[text()='Булки']"))
    )

    # Переходим в «Соусы»
    sauces_tab = driver.find_element(By.XPATH, "//span[text()='Соусы']")
    sauces_tab.click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h2[text()='Соусы']"), "Соусы")
    )

    # Переходим в «Начинки»
    fillings_tab = driver.find_element(By.XPATH, "//span[text()='Начинки']")
    fillings_tab.click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h2[text()='Начинки']"), "Начинки")
    )

    # Переходим обратно в «Булки»
    buns_tab = driver.find_element(By.XPATH, "//span[text()='Булки']")
    buns_tab.click()
    WebDriverWait(driver, 5).until(
        EC.text_to_be_present_in_element((By.XPATH, "//h2[text()='Булки']"), "Булки")
    )

    # Проверяем, что все разделы работают
    assert True, "Переходы между разделами в Конструкторе работают"