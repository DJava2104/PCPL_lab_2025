# test_rk1.py
import unittest
from rk1_refactored import DataModule, QueryModule, DataColumn, DataTable, ColumnTable

class TestRK1Module(unittest.TestCase):
    """Тесты для модулей РК1"""
    
    def setUp(self):
        """Подготовка тестовых данных"""
        self.tables, self.columns, self.column_tables = DataModule.create_test_data()
        self.query_module = QueryModule()
    
    def test_query_1_returns_correct_columns(self):
        """Тест запроса 1: возвращает колонки с 'id' в конце"""
        result = self.query_module.query_1(self.tables, self.columns)
        
        # Проверяем количество найденных колонок
        self.assertEqual(len(result), 4)
        
        # Проверяем конкретные значения
        expected_columns = ['user_id', 'product_id', 'account_id', 'analytics_id']
        result_columns = [col_name for col_name, _ in result]
        
        self.assertListEqual(sorted(result_columns), sorted(expected_columns))
        
        # Проверяем, что каждая колонка имеет связанную таблицу
        for col_name, table_name in result:
            self.assertIsNotNone(col_name)
            self.assertIsNotNone(table_name)
            self.assertTrue(col_name.lower().endswith('id'))
    
    def test_query_2_calculates_average_correctly(self):
        """Тест запроса 2: корректно вычисляет среднее значение"""
        result = self.query_module.query_2(self.tables, self.columns)
        
        # Проверяем количество таблиц
        self.assertEqual(len(result), 5)
        
        # Проверяем сортировку по возрастанию
        sizes = [size for _, size in result]
        self.assertEqual(sizes, sorted(sizes))
        
        # Проверяем конкретное вычисление для таблицы "Orders"
        orders_result = [item for item in result if item[0] == "Orders"]
        self.assertEqual(len(orders_result), 1)
        
        # sale_date(20) + amount(10) = 30 / 2 = 15.0
        table_name, avg_size = orders_result[0]
        self.assertEqual(table_name, "Orders")
        self.assertAlmostEqual(avg_size, 15.0)
    
    def test_query_3_finds_tables_starting_with_A(self):
        """Тест запроса 3: находит таблицы, начинающиеся с 'А'"""
        result = self.query_module.query_3(self.tables, self.columns, self.column_tables)
        
        # Проверяем, что найдена только таблица "Аналитика"
        self.assertEqual(len(result), 1)
        
        table_info = result[0]
        self.assertEqual(table_info['table'], "Аналитика")
        
        # Проверяем, что колонки найдены
        self.assertGreater(len(table_info['columns']), 0)
        
        # Проверяем, что все ожидаемые колонки присутствуют
        expected_columns = ['user_id', 'product_id', 'sale_date', 'analytics_id', 'report_name']
        for col in expected_columns:
            self.assertIn(col, table_info['columns'])
        
        # Проверяем количество колонок
        self.assertEqual(len(table_info['columns']), 5)

class TestDataClasses(unittest.TestCase):
    """Тесты для классов данных"""
    
    def test_datacolumn_creation(self):
        """Тест создания объекта DataColumn"""
        column = DataColumn(1, "test_column", 100, 1)
        self.assertEqual(column.column_id, 1)
        self.assertEqual(column.name, "test_column")
        self.assertEqual(column.data_size, 100)
        self.assertEqual(column.table_id, 1)
    
    def test_datatable_creation(self):
        """Тест создания объекта DataTable"""
        table = DataTable(1, "TestTable")
        self.assertEqual(table.table_id, 1)
        self.assertEqual(table.table_name, "TestTable")
    
    def test_columntable_creation(self):
        """Тест создания объекта ColumnTable"""
        link = ColumnTable(1, 2)
        self.assertEqual(link.column_id, 1)
        self.assertEqual(link.table_id, 2)

if __name__ == '__main__':
    unittest.main()