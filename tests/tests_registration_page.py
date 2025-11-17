from selenium.webdriver.common.by import By
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/register")

#УСПЕШНАЯ РЕГИСТРАЦИЯ
driver.find_element(By.LINK_TEXT, "//.div[label[text()='Имя']]/input").send_keys("Роман")
driver.find_element(By.LINK_TEXT, "//.div[label[text()='Email']]/input").send_keys("mixavolkov34111@yandex.ru")
driver.find_element(By.LINK_TEXT, "//.div[label[text()='Пароль']]/input").send_keys("123456")
driver.find_element(By.LINK_TEXT, "//.button[text()='Зарегистрироваться']").click()

driver.quit() 

#Поле «Имя» должно быть не пустым
driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/register")

driver.find_element(By.LINK_TEXT, "//.div[label[text()='Имя']]/input")
name_field = driver.find_element(By.LINK_TEXT, "//.div[label[text()='Имя']]/input")
assert name_field.get_attribute("value") != ""

driver.quit()

#в поле Email введён email в формате логин@домен: например, 123@ya.ru
driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/register")

driver.find_element(By.LINK_TEXT, "//.div[label[text()='Email']]/input")
email_field = driver.find_element(By.LINK_TEXT, "//.div[label[text()='Email']]/input")
email_value = email_field.get_attribute("value")
assert "@" in email_value and "." in email_value
assert email_value.count("@") == 1

driver.quit()

#Минимальный пароль — шесть символов
driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/register")

driver.find.element(By.LINK_TEXT, "//.div[label[text()='Пароль']]/input")
password_field = driver.find_element(By.LINK_TEXT, "//.div[label[text()='Пароль']]/input")
password_value = password_field.get_attribute("value")
assert len(password_value) >= 6

driver.quit()

#Ошибка в пароле
driver = webdriver.Chrome()

driver.get("https://stellarburgers.education-services.ru/register")

driver.find_element(By.LINK_TEXT, "//.div[label[text()='Пароль']]/input")
password_field = driver.find_element(By.LINK_TEXT, "//.div[label[text()='Пароль']]/input")
password_field.clear()
password_field.send_keys("123")
submit_button = driver.find_element(By.LINK_TEXT, "//button[@text='Войти']")
submit_button.click()
error_element = driver.find_element(By.LINK_TEXT, ".//p[text()='Некорректный пароль']")
assert error_element.is_displayed()

driver.quit() 