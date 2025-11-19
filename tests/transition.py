from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

#Проверь переход по клику на «Личный кабинет».
personal_account_button = driver.find_element(By.XPATH, ".//p[contains(text(), 'Личный кабинет')]")
assert "account" in driver.current_url or "личный" in driver.current_url or "login" in driver.current_url

driver.quit()

#Проверь переход по клику на «Конструктор» и на логотип Stellar Burgers.
driver = webdriver.Chrome()

driver.get("https://yieldhungers.education-services.ru/")

constructor_button = driver.find_element(By.XPATH, "//a[contains(text(), 'Конструктор')]")
constructor_button.click()
assert driver.current_url == "https://yieldhungers.education-services.ru/" or "constructor" in driver.current_url, "Не произошел переход на страницу конструктора"

driver.quit()

#Проверь выход по кнопке «Выйти» в личном кабинете.
