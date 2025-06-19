import csv
from typing import List, Dict, Union

class CSVProcessor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = self._load_csv()
        self.headers = self.data[0].keys() if self.data else []
    
    def _load_csv(self) -> List[Dict[str, Union[str, float]]]:
        with open(self.file_path, mode='r', encoding='utf-8') as file:
            return list(csv.DictReader(file))
    
    def _convert_value(self, value: str, column: str) -> Union[str, float, int]:
        try:
            return float(value) if '.' in value else int(value)
        except ValueError:
            return value
    
    def filter_data(
        self, 
        column: str, 
        operator: str, 
        value: str
    ) -> List[Dict[str, Union[str, float]]]:
        if column not in self.headers:
            raise ValueError(f"Колонка '{column}' не найдена")
        
        filter_value = self._convert_value(value, column)
        
        operators = {
            '>': lambda x, y: x > y,
            '<': lambda x, y: x < y,
            '=': lambda x, y: x == y,
            '>=': lambda x, y: x >= y,
            '<=': lambda x, y: x <= y,
            '!=': lambda x, y: x != y,
        }
        
        if operator not in operators:
            raise ValueError(f"Неподдерживаемый оператор: '{operator}'")
        
        filtered_data = []
        for row in self.data:
            row_value = self._convert_value(row[column], column)
            
            try:
                if operators[operator](row_value, filter_value):
                    filtered_data.append(row)
            except TypeError:
                continue
        
        return filtered_data
    
    def aggregate_data(
        self, 
        column: str, 
        operation: str
    ) -> Dict[str, Union[str, float]]:
        if column not in self.headers:
            raise ValueError(f"Колонка '{column}' не найдена")
        
        numeric_values = []
        for row in self.data:
            try:
                numeric_value = float(row[column])
                numeric_values.append(numeric_value)
            except ValueError:
                continue
        
        if not numeric_values:
            raise ValueError(f"Нет числовых значений в колонке '{column}'")
        
        operations = {
            'avg': lambda x: sum(x) / len(x),
            'min': min,
            'max': max,
            'sum': sum,
            'count': len,
        }
        
        if operation not in operations:
            raise ValueError(f"Неподдерживаемая операция: '{operation}'")
        
        return {
            'column': column,
            'operation': operation,
            'result': operations[operation](numeric_values)
        }