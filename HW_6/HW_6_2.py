#2. Замыкание для проверки времени выполнения. Напишите функцию
#create_time_checker(max_time), которая возвращает вложенную
#функцию для проверки времени выполнения теста. Вложенная функция
#принимает фактическое время выполнения и сообщает, превышен
#установленный лимит или нет. Создайте два независимых замыкания с
#разными значениями max_time и продемонстрируйте их работу

def create_time_checker(max_time):
    def time_fact(actual_time):
        if actual_time > max_time:
            return f"Время выполнения ({actual_time} сек) превысило лимит ({max_time} )"
        else:
            return f"Время выполнения ({actual_time} сек) не превышено."
    return time_fact

test_fackt_1 = create_time_checker(1.5)
test_fackt_2 = create_time_checker(10.0)

print(test_fackt_1(3.5))
print(test_fackt_2(4.5))

