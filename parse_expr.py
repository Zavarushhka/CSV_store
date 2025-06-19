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