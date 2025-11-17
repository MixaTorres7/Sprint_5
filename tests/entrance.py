from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/register")

#войти в аккаунт
driver.find_element(By.LINK_TEXT, "//.div[label[text()='Email']]/input").send_keys("mixavolkov34111@yandex.ru")
driver.find_element(By.LINK_TEXT, "//.div[label[text()='Пароль']]/input").send_keys("123456")
driver.find_element(By.LINK_TEXT, ".//buttom[text()='Войти']").click()
driver.quit()

#Вход по кнопке "Личный кабинет"
driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/")

driver.find_element(By.LINK_TEXT, ".//p[text()='Личный кабинет']").click()
driver.quit()

#ВХОД ЧЕРЕЗ КНОПКУ ПО ФОРМЕ РЕГИСТРАЦИИ
driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/login")

driver.find_element(By.LINK_TEXT, ".//a[text()='Зарегистрироваться']").click()
driver.quit()

#вход через кнопку в форме восстановления пароля.
driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/login")

driver.find_element(By.LINK_TEXT, ".//a[text()='Восстановить пароль']").click()
driver.quit()