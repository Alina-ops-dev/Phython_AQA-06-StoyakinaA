# 1Пользователь одной строкой вводит результаты запуска автотестов через
# пробел, например: PASS FAIL PASS SKIP PASS FAIL. Программа должна
# преобразовать введенную строку в список, подсчитать количество тестов
# каждого типа и вывести общую статистику. Логику подсчета необходимо
# вынести в отдельную функцию get_test_statistics(results), которая
# возвращает результат в виде словаря. Дополнительно программа должна
# вывести процент успешно пройденных тестов относительно общего
# количества тестов.
# Пример вывода:
# Всего тестов: 6
# PASS: 3
# FAIL: 2
# SKIP: 1
# Успешно: 50.0%


def get_test_statistics(results):
    statuses = {
        "PASS": results.count("PASS"),
        "FAIL": results.count("FAIL"),
        "SKIP": results.count("SKIP")
    }
    return statuses

user_input = input("Введите результаты тестов через пробел: ")
test_list = []
for status in user_input.split():
    upper_status = status.upper()
    test_list.append(upper_status)

if test_list:
    statistics = get_test_statistics(test_list)
    total_tests = len(test_list)
    success_rate = (statistics["PASS"] / total_tests) * 100
    rounded_rate = round(success_rate, 1)

    print(f"Всего тестов: {total_tests}")
    print(f"PASS: {statistics['PASS']}")
    print(f"FAIL: {statistics['FAIL']}")
    print(f"SKIP: {statistics['SKIP']}")
    print(f"Успешно: {rounded_rate}%")
