import random
import string

def generate_random_email():
    """Генерирует случайный email для регистрации"""
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{username}@{domain}.ru"

def generate_random_password(length=6):
    """Генерирует случайный пароль заданной длины"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_name():
    """Генерирует случайное имя"""
    names = ['Иван', 'Мария', 'Петр', 'Анна', 'Сергей', 'Ольга', 'Алексей', 'Елена']
    return random.choice(names)

class TestData:
    VALID_USER = {
        "name": "Роман",
        "email": "mixavolkov34112@yandex.ru",
        "password": "123456" 
    }
    
    EXISTING_USER = {
        "name": "Роман",
        "email": "mixavolkov34111@yandex.ru",  # Твой реальный email
        "password": "123456"  # Твой реальный пароль
    }
    
    INVALID_PASSWORD_USER = {
        "name": "Роман",
        "email": "mixavolkov34111@yandex.ru",
        "password": "123"  # Слишком короткий пароль
    }