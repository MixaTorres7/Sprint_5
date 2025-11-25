from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_LINK = (By.XPATH, "//p[text()='Личный Кабинет']")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    LOGO = (By.XPATH, "//div[contains(@class, 'logo')]")
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")
    BUNS_HEADER = (By.XPATH, "//h2[text()='Булки']")
    SAUCES_HEADER = (By.XPATH, "//h2[text()='Соусы']")
    FILLINGS_HEADER = (By.XPATH, "//h2[text()='Начинки']")

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@type='text' and @name='name'] | //input[@name='email']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//input[@name='name'] | //label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//input[@name='email'] | //label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//input[@name='password'] | //label[contains(text(), 'Пароль')]/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')] | //button[@type='submit']")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(@class, 'input__error')] | //div[contains(@class, 'error')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')] | //a[@href='/login']")

class PersonalAccountLocators:
    PROFILE_LINK = (By.XPATH, "//a[contains(@href, 'profile')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")

class ForgotPasswordLocators:
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")