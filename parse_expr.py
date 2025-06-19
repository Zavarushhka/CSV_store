'''
Модуль для парсинга выражений фильтрации и агрегации данных.

Основные функции
    1.  parse_filter_expr(expression) - разбирает строку условия фильтрации
        на составляющие: имя колонки, оператор сравнения и значения.
        Поддерживаемые операторы: >, <, >=, <=, -, !=
        Пример: "age >= 25" -> ("age", ">=", "25")

    2.  parse_aggregate_expr(expression) - разбирает строку агрегации
        на имя колонки и тип агрегации.
        Поддерживаемые операции: min, max, avg
        Пример: "price=avg" -> ("price", "avg")

Обе функции возвращают кортежи строк и автоматически удаляют лишние пробелы,
путем регулярных выражений.
В случае ошибок формата вызываются ValueError.
'''

import re

def parse_filter_expr(expression: str) -> tuple[str, str, str]:
    pattern = r'\s*(>=|<=|!=|>|<|=)\s*'
    match = re.split(pattern, expression, maxsplit=1)
    if len(match) != 3:
        raise ValueError(f"Некорректный формат фильтра: {expression}")
    
    column, operator, value = match
    return column.strip(), operator, value.strip()

def parse_aggregate_expr(expression: str) -> tuple[str, str]:
    
    parts = expression.split('=', maxsplit=1)
    if len(parts) != 2:
        raise ValueError(f"Некорректный формат агрегации: {expression}")
    
    column, operation = parts
    return column.strip(), operation.strip()