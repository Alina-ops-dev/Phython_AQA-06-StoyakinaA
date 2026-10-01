#1.Рекурсивный подсчет результатов тестов. Дан список результатов
#автотестов со статусами PASS, FAIL и SKIP. Напишите рекурсивную
#функцию, которая подсчитывает количество тестов со статусом PASS.
#Функция должна обрабатывать список с помощью рекурсии.
#Использовать циклы for и while нельзя.

test_results = ['PASS', 'PASS', 'FAIL', 'SKIP', 'FAIL', 'PASS']


def function(n):
    if not n:
        return 0

    if n[0] == 'PASS':
        first = 1
    else:
        first = 0
    return first + function(n[1:])


total_pass = function(test_results)
print(f"Количество успешных тестов: {total_pass}")