#3. Декоратор для логирования автотестов. Напишите декоратор log_test,
#который перед запуском тестовой функции выводит её имя, после
#выполнения сообщает о завершении и выводит полученный результат.
#Декоратор должен поддерживать функции с произвольным количеством
#позиционных и именованных аргументов с помощью *args и **kwargs.
#Используйте functools.wraps(), чтобы сохранить метаданные исходной
#функции.



import functools

def log_test(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f" Запуск {func.__name__} ---")
        res = func(*args, **kwargs)
        print(f" Стоп {func.__name__} -> {res}\n")
        return res
    return wrapper

@log_test
def test_smoke():
    return "PASS"

@log_test
def test_login(username, password):
    return f"PASS: {username} вошёл с паролем длиной {len(password)}"

test_smoke()
test_login("user", "qwerty123")