#5. Результаты автотестов. Пользователь вводит количество выполненных
#автотестов, а затем по очереди результат каждого теста: PASS, FAIL или
#SKIP. Программа должна подсчитать количество тестов с каждым
#статусом и вывести итоговую статистику. Если присутствует хотя бы один
#FAIL, необходимо сообщить о наличии упавших тестов; если FAIL
#отсутствуют - сообщить об успешном прохождении выполненных тестов.
#Любой неизвестный статус необходимо пропустить и не учитывать в
#статистике.

statuses = int(input("Введите количество автотестов:"))
pass_count = fail_count = skip_count = 0
current_test = 1

while current_test <= statuses:
    status = input(f"Результат теста {current_test} (в формате FAIL, PASS, SKIP):").upper()

    if status == "PASS":
        pass_count += 1
    elif status == "FAIL":
        fail_count += 1
    elif status == "SKIP":
        skip_count += 1
    else:
        print("Неизвестный статус. Повторите ввод.")
        continue
    current_test += 1

print(f"\nСтатистика:\nPASS: {pass_count}\nFAIL: {fail_count}\nSKIP: {skip_count}")

# Короткая проверка условия одной строкой
print("Есть упавшие тесты!" if fail_count > 0 else "Все тесты прошли успешно!")