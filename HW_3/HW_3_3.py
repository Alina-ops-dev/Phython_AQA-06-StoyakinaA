#3. Дан список тестов:
#tests = [
#"test_login",
#"test_logout",
#"test_registration",
#"test_profile",
#"test_payment",
#"test_search"
#]
#Пользователь вводит количество тестов, которые необходимо запустить.
#Программа должна случайным образом выбрать указанное количество
#уникальных тестов из списка и каждому выбранному тесту случайно
#назначить статус PASS, FAIL или SKIP. Результаты необходимо объединить
#и вывести в виде отчёта. Если пользователь запросил больше тестов, чем
#существует в списке, программа должна вывести сообщение об ошибке.

import random

tests = [
    "test_login",
    "test_logout",
    "test_registration",
    "test_profile",
    "test_payment",
    "test_search"
]
statuses = [
    "PASS",
    "FAIL",
    "SKIP"
]

test_count = int(input("Введите количество тестов: "))
if test_count  > len(tests):
    print("Ошибка: количество тестов превышает количество в списке")
elif test_count <= 0:
    print("Ошибка: число должно быть больше нуля")
else:
    test = random.sample(tests, test_count)
    for test in test:
        random_status = random.choice(statuses)
        print(f"{test} — {random_status}")

