#2. Есть два списка:
#test_cases = ["Login", "Registration", "Checkout", "Logout"]
#statuses = ["PASS", "FAIL", "PASS", "SKIP"]
#Необходимо с помощью zip() объединить название каждого тест-кейса с
#его статусом. Создайте функцию print_report(test_cases, statuses),
#которая принимает два списка и выводит отчёт в формате Login — PASS.
#После формирования отчета программа должна определить количество
#успешных и неуспешных тестов и сообщить, можно ли считать тестовый запуск успешным
# если есть хотя бы один FAIL, запуск считается неуспешным.

test_cases = ["Login", "Registration", "Checkout", "Logout"]
statuses = ["PASS", "FAIL", "PASS", "SKIP"]

def print_report(test_cases, statuses):
    for name, status in zip(test_cases, statuses):
        print(f"{name} - {status}")
print_report(test_cases, statuses)

pass_count = statuses.count("PASS")
fail_count = statuses.count("FAIL")
skip_count = statuses.count("SKIP")

print(f"Успешных тестов (PASS): {pass_count}")
print(f"Неуспешных тестов (FAIL): {fail_count}")
print(f"Пропущенных тестов (SKIP): {skip_count}")

if fail_count > 0:
    print("Отчет неуспешный")
else:
    print("Отчет успешный")