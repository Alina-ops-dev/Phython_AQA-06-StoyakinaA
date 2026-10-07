#Создайте JSON-файл с тестовыми пользователями для проверки
#авторизации. Для каждого пользователя должны храниться логин, пароль
#и ожидаемый результат авторизации. Напишите программу, которая
#открывает JSON-файл, загружает данные и выводит информацию о
#каждом тестовом пользователе. Программа должна корректно
#обрабатывать ситуации, когда файл не существует, содержимое файла
#невозможно прочитать как JSON или у пользователя отсутствует
#обязательное поле. Для обработки ошибок используйте try/except,
#соответствующие типы исключений и получение информации об ошибке
#через as e.

import json

filename = 'users.json'

try:
    with open(filename, "r", encoding="utf-8") as f:
        users_data = json.load(f)

    for user in users_data:
        try:
            login = user['login']
            password = user['password']
            result = user['expected_result']
            print(f"Логин: {login}, Пароль: {password}, Ожидаемый результат: {result}")

        except KeyError as e:
            print(f"Ошибка в данных пользователя!\n"
                  f"Отсутствует обязательное поле: {e}\n")

except FileNotFoundError as e:
    print(f"Файл не найден!{e}")

except json.JSONDecodeError as e:
    print(f"Невозможно прочитать файл как JSON: {e}")
