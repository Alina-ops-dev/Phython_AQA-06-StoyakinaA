#Дан список результатов автотестов. Для каждого теста известны его
#название, статус выполнения (PASS, FAIL или SKIP) и время выполнения.
#Напишите программу, которая с помощью filter() получает все
#упавшие тесты, с помощью map() формирует список их названий, а с
#помощью reduce() рассчитывает общее время выполнения всех тестов.
#Дополнительно с помощью генератор списка сформируйте список
#названий успешно пройденных тестов. В результате программа должна
#вывести количество тестов каждого статуса, список названий упавших
#тестов, список успешно пройденных тестов и общее время выполнения
#всех тестов.

from functools import reduce

test_results = [
    {"name": "Тест авторизации", "status": "PASS", "time": 1.5},
    {"name": "Тест корзины", "status": "FAIL", "time": 3.2},
    {"name": "Тест оплаты", "status": "SKIP", "time": 0.0},
    {"name": "Тест поиска", "status": "PASS", "time": 0.8},
    {"name": "Тест профиля", "status": "FAIL", "time": 2.1},
    {"name": "Тест уведомлений", "status": "PASS", "time": 1.2}
]


failed_tests_status = list(filter(lambda x: x["status"] == "FAIL", test_results))

failed_test_names = list(map(lambda x: x["name"], failed_tests_status))

passed_test_names = [x["name"] for x in test_results if x["status"] == "PASS"]

all_times = [x["time"] for x in test_results]
total_execution_time = reduce(lambda a, b: a + b, all_times)

statuses = [x["status"] for x in test_results]
pass_count = statuses.count("PASS")
fail_count = statuses.count("FAIL")
skip_count = statuses.count("SKIP")

print(f"Количество тестов:")
print(f"  - PASS: {pass_count}")
print(f"  - FAIL: {fail_count}")
print(f"  - SKIP: {skip_count}")
print(f"Список названий упавших тестов: {failed_test_names}")
print(f"Список успешно пройденных тестов: {passed_test_names}")
print(f"Общее время выполнения всех тестов: {total_execution_time} сек.")