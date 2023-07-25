import random

list_items = "qwertyuiopasdfghjklzxcvbnm1234567890,./!@#$%^*&()_"


def generate_password(num):
    password = []
    for i in range(num):
        password.append(random.choice(list(list_items)))
    return ''.join(password)

lenth_password = int(input("Введите длину для вашего пароля: "))

print(F"Вот такой пароль у вас получился: {generate_password(lenth_password)}")

