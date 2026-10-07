#4. Декоратор повторного запуска. Напишите декоратор с параметром
#retry(count), который повторно запускает декорируемую функцию
#указанное количество раз, пока функция не вернет True. Перед каждой
#попыткой необходимо выводить её номер. Если функция вернула True,
#дальнейшие попытки выполнять не нужно. Декоратор должен
#поддерживать передачу позиционных и именованных аргументов через
#*args и **kwargs.

import functools

def retry(count):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = None
            for i in range(1, count + 1):
                print(f"Попытка {i}")
                res = func(*args, **kwargs)
                if res is True:
                    return res
            return res
        return wrapper
    return decorator


@retry(3)
def prohodit():
    return True


@retry(3)
def ne_prohodit():
    return False


@retry(3)
def login(user, password):
    return user == "admin" and password == "1234"


print("prohodit:", prohodit())
print("ne_prohodit:", ne_prohodit())
print("login:", login(password="1234", user="admin"))