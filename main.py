import os
import argparse
from tabulate import tabulate
from parse_expr import *
from csv_processor import CSVProcessor

parser = argparse.ArgumentParser(
    description='Обработка CSV файлов',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
    
parser.add_argument(
    '--file',
    required=True,
    help='Путь к CSV файлу (например: --file data.csv)'
)
    
parser.add_argument(
    '--where',
    help="Фильтрация в формате 'колонкаоператорзначение' (пример: --filter 'price>100')"
)
    
parser.add_argument(
    '--aggregate',
    help="Агрегация в формате 'колонка=операция' (пример: --aggregate 'price=avg')"
)
    
args = parser.parse_args()
    
try:
    if not os.path.exists(args.file):
        raise FileNotFoundError(f"Файл {args.file} не найден")
        
    processor = CSVProcessor(args.file)
        
    if args.where:
        column, operator, value = parse_filter_expr(args.where)
        filtered_data = processor.filter_data(column, operator, value)
        print(tabulate(filtered_data, headers="keys", tablefmt="grid"))
            
    elif args.aggregate:
        column, operation = parse_aggregate_expr(args.aggregate)
        result = processor.aggregate_data(column, operation)
        print(tabulate([result], headers="keys", tablefmt="grid"))
            
    else:
        print(tabulate(processor.data, headers="keys", tablefmt="grid"))
            
except Exception as e:
    print(f"Ошибка: {e}")