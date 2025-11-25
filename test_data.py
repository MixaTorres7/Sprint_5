import random
import string

def generate_random_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))
    return f"{username}@{domain}.ru"

def generate_random_password(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_name():
    names = ['Иван', 'Мария', 'Петр', 'Анна', 'Сергей', 'Ольга', 'Алексей', 'Елена']
    return random.choice(names)

class TestData:
    EXISTING_USER = {
        "name": "Роман",
        "email": "mixavolkov34111@yandex.ru",
        "password": "123456"
    }
    
    INVALID_PASSWORD_USER = {
        "name": "Роман",
        "email": "mixavolkov34111@yandex.ru",
        "password": "123"
    }