# rk1_refactored.py
class DataColumn:
    """Класс Колонка данных (аналог Сотрудника)"""
    def __init__(self, column_id, name, data_size, table_id):
        self.column_id = column_id
        self.name = name
        self.data_size = data_size  # количественный признак (размер данных в МБ)
        self.table_id = table_id
    
    def __repr__(self):
        return f"DataColumn({self.column_id}, '{self.name}', {self.data_size}, {self.table_id})"

class DataTable:
    """Класс Таблица данных (аналог Отдела)"""
    def __init__(self, table_id, table_name):
        self.table_id = table_id
        self.table_name = table_name
    
    def __repr__(self):
        return f"DataTable({self.table_id}, '{self.table_name}')"

class ColumnTable:
    """Класс для связи многие-ко-многим"""
    def __init__(self, column_id, table_id):
        self.column_id = column_id
        self.table_id = table_id
    
    def __repr__(self):
        return f"ColumnTable({self.column_id}, {self.table_id})"

# Модуль данных
class DataModule:
    """Модуль для работы с данными"""
    @staticmethod
    def create_test_data():
        """Создание тестовых данных"""
        tables = [
            DataTable(1, "Users"),
            DataTable(2, "Products"),
            DataTable(3, "Аналитика"),
            DataTable(4, "Orders"),
            DataTable(5, "Accounts")
        ]
        
        columns = [
            DataColumn(1, "user_id", 50, 1),
            DataColumn(2, "username", 30, 1),
            DataColumn(3, "user_email", 40, 1),
            DataColumn(4, "product_id", 60, 2),
            DataColumn(5, "product_name", 25, 2),
            DataColumn(6, "price", 15, 2),
            DataColumn(7, "sale_date", 20, 4),
            DataColumn(8, "amount", 10, 4),
            DataColumn(9, "account_id", 35, 5),
            DataColumn(10, "balance", 12, 5),
            DataColumn(11, "analytics_id", 45, 3),
            DataColumn(12, "report_name", 22, 3)
        ]
        
        column_tables = [
            ColumnTable(1, 1),  # user_id в Users
            ColumnTable(2, 1),  # username в Users
            ColumnTable(3, 1),  # user_email в Users
            ColumnTable(4, 2),  # product_id в Products
            ColumnTable(5, 2),  # product_name в Products
            ColumnTable(6, 2),  # price в Products
            ColumnTable(7, 4),  # sale_date в Orders
            ColumnTable(8, 4),  # amount в Orders
            ColumnTable(9, 5),  # account_id в Accounts
            ColumnTable(10, 5), # balance в Accounts
            ColumnTable(11, 3), # analytics_id в Аналитика
            ColumnTable(12, 3), # report_name в Аналитика
            # Дополнительные связи для многие-ко-многим
            ColumnTable(1, 3),  # user_id также в Аналитика
            ColumnTable(4, 3),  # product_id также в Аналитика
            ColumnTable(7, 3),  # sale_date также в Аналитика
        ]
        
        return tables, columns, column_tables

# Модуль запросов
class QueryModule:
    """Модуль для выполнения запросов"""
    
    @staticmethod
    def query_1(tables, columns):
        """Колонки с названием, оканчивающимся на 'id' и их таблицы"""
        result_lc = [
            (column.name, next(t.table_name for t in tables if t.table_id == column.table_id))
            for column in columns 
            if column.name.lower().endswith('id')
        ]
        return result_lc
    
    @staticmethod
    def query_2(tables, columns):
        """Средний размер данных колонок по таблицам"""
        table_stats = {}
        
        for column in columns:
            if column.table_id not in table_stats:
                table_stats[column.table_id] = {'total_size': 0, 'count': 0}
            table_stats[column.table_id]['total_size'] += column.data_size
            table_stats[column.table_id]['count'] += 1
        
        result = []
        for table_id, stats in table_stats.items():
            table = next(t for t in tables if t.table_id == table_id)
            avg_size = stats['total_size'] / stats['count']
            result.append((table.table_name, avg_size))
        
        result.sort(key=lambda x: x[1])
        return result
    
    @staticmethod
    def query_3(tables, columns, column_tables):
        """Таблицы с названием на 'А' и их колонки (связь многие-ко-многим)"""
        a_tables = [t for t in tables if t.table_name.startswith('А')]
        
        result = []
        for table in a_tables:
            table_column_ids = [ct.column_id for ct in column_tables if ct.table_id == table.table_id]
            table_columns = [col for col in columns if col.column_id in table_column_ids]
            
            result.append({
                'table': table.table_name,
                'columns': [col.name for col in table_columns]
            })
        
        return result

# Основной модуль
def main():
    """Главная функция приложения"""
    print("=== РУБЕЖНЫЙ КОНТРОЛЬ №1 ===")
    print("Вариант 32: Колонка данных - Таблица данных")
    print()
    
    # Создание тестовых данных
    tables, columns, column_tables = DataModule.create_test_data()
    query_module = QueryModule()
    
    print("\n" + "="*50)
    print("ЗАПРОС 1: Колонки с названием, оканчивающимся на 'id', и их таблицы")
    result1 = query_module.query_1(tables, columns)
    for col_name, table_name in result1:
        print(f"  Колонка: {col_name}, Таблица: {table_name}")
    
    print("\n" + "="*50)
    print("ЗАПРОС 2: Таблицы со средним размером данных колонок")
    result2 = query_module.query_2(tables, columns)
    for table_name, avg_size in result2:
        print(f"  Таблица: {table_name}, Средний размер: {avg_size:.2f} МБ")
    
    print("\n" + "="*50)
    print("ЗАПРОС 3: Таблицы с названием на 'А' и их колонки (связь многие-ко-многим)")
    result3 = query_module.query_3(tables, columns, column_tables)
    for item in result3:
        print(f"  Таблица: {item['table']}")
        print(f"    Колонки: {', '.join(item['columns'])}")

if __name__ == "__main__":
    main()