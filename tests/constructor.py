from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://yieldhungers.education-services.ru/")

# Проверь переход к разделу "Булки"
buns_section = driver.find_element(By.XPATH, "//span[contains(text(), 'Булки')]")
buns_section.click()

# Проверь, что активен раздел "Булки"
active_buns = driver.find_element(By.XPATH, "//div[contains(@class, 'active')]//span[contains(text(), 'Булки')]")
assert active_buns.is_displayed(), "Раздел 'Булки' не стал активным"

# Проверь переход к разделу "Соусы"
sauces_section = driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]")
sauces_section.click()

# Проверь, что активен раздел "Соусы"
active_sauces = driver.find_element(By.XPATH, "//div[contains(@class, 'active')]//span[contains(text(), 'Соусы')]")
assert active_sauces.is_displayed(), "Раздел 'Соусы' не стал активным"

# Проверь переход к разделу "Начинки"
fillings_section = driver.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]")
fillings_section.click()

# Проверь, что активен раздел "Начинки"
active_fillings = driver.find_element(By.XPATH, "//div[contains(@class, 'active')]//span[contains(text(), 'Начинки')]")
assert active_fillings.is_displayed(), "Раздел 'Начинки' не стал активным"

# Закрой браузер
driver.quit()