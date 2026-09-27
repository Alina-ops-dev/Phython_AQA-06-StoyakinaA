#Cоздайте программу для формирования отчёта по результатам
#автоматизированного тестирования. Исходные данные программа
# получать из JSON-файла, в котором для каждого теста указаны
#название, статус и время выполнения. Программа должна определить
#общее количество тестов, количество тестов со статусами PASS, FAIL и
#SKIP, сформировать список упавших тестов, определить самый
#длительный тест и рассчитать суммарное время выполнения. При
#обработке данных необходимо использовать минимум один генератор
#списка, lambda, filter() и reduce(). Работу с файлом и входными
#данными необходимо защитить с помощью try/except: программа
#должна корректно обрабатывать отсутствие файла, некорректный JSON и
#неправильную структуру тестовых данных. Сформированный итоговый
#отчёт необходимо сохранить в отдельный JSON-файл.

import json
from functools import reduce

inp_f, out_f = "test_data.json", "test_report.json"

try:
    with open(inp_f, "r", encoding="utf-8") as f:
        tests = json.load(f)
    if not isinstance(tests, list):
        raise ValueError("JSON должен быть списком.")

    failed_names = [t["name"] for t in filter(lambda t: t["status"] == "FAIL", tests)]
    total_time = reduce(lambda total, t: total + t["duration"], tests, 0)
    longest = max(tests, key=lambda t: t["duration"]) if tests else {"name": None, "duration": 0}

    report = {
        "total_tests": len(tests),
        "metrics": {s: sum(1 for t in tests if t["status"] == s) for s in ["PASS", "FAIL", "SKIP"]},
        "failed_test_names": failed_names,
        "longest_test": {"name": longest["name"], "duration": longest["duration"]},
        "total_duration": round(total_time, 2)
    }

    with open(out_f, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=4)
    print(f" Отчет сохранен в '{out_f}'")

except FileNotFoundError as e:
    print(e)
except json.JSONDecodeError as e:
    print(e)
except (KeyError, TypeError, ValueError) as e:
    print(e)