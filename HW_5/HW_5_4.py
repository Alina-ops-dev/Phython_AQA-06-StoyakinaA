#Создайте собственное исключение InvalidTestStatusError,
# от Exception. Напишите функцию, которая принимает статус
#теста и проверяет его значение. Допустимыми считаются только PASS,
#FAIL и SKIP. Если передан любой другой статус, функция должна с
#помощью raise создать InvalidTestStatusError и передать в него
#сообщение с некорректным значением. В основной программе
#обработайте это исключение через try/except и выведите понятное
#сообщение пользователю. Проверьте программу как с корректными, так и
# некорректными статусами.

class InvalidTestStatusError(Exception):
    pass

def status_test(status):
    if status.strip().upper() not in ["PASS", "FAIL", "SKIP"]:
        raise InvalidTestStatusError(f"Некорректный статус: '{status}'. Разрешены только: PASS, FAIL, SKIP")
    print(f"Статус '{status.strip().upper()}' успешно принят.")


try:
    statuses = input("Введите статус: ")
    status_test(statuses)
except InvalidTestStatusError as e:
    print(f"Ошибка: {e}")