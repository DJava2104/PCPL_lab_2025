"""
Модульные тесты с использованием TDD подхода (unittest)
"""
import unittest
import os
from calculator import Calculator, FileProcessor

class TestCalculatorTDD(unittest.TestCase):
    """Класс для TDD тестирования калькулятора"""
    
    def setUp(self):
        """Инициализация перед каждым тестом"""
        self.calc = Calculator()
        self.file_processor = FileProcessor()
    
    def tearDown(self):
        """Очистка после каждого теста"""
        # Удаляем тестовые файлы, если они существуют
        test_files = ['test_input.txt', 'test_output.txt']
        for file in test_files:
            if os.path.exists(file):
                os.remove(file)
    
    # Тест 1: Проверка сложения
    def test_add_positive_numbers(self):
        """Тест сложения положительных чисел"""
        result = self.calc.add(5, 3)
        self.assertEqual(result, 8)
        self.assertIsInstance(result, (int, float))
    
    def test_add_negative_numbers(self):
        """Тест сложения отрицательных чисел"""
        result = self.calc.add(-5, -3)
        self.assertEqual(result, -8)
    
    def test_add_mixed_numbers(self):
        """Тест сложения положительного и отрицательного числа"""
        result = self.calc.add(5, -3)
        self.assertEqual(result, 2)
    
    # Тест 2: Проверка деления
    def test_divide_normal(self):
        """Тест обычного деления"""
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
    
    def test_divide_by_zero(self):
        """Тест деления на ноль"""
        with self.assertRaises(ValueError) as context:
            self.calc.divide(10, 0)
        self.assertEqual(str(context.exception), "Деление на ноль невозможно")
    
    def test_divide_float_result(self):
        """Тест деления с результатом-дробью"""
        result = self.calc.divide(5, 2)
        self.assertEqual(result, 2.5)
    
    # Тест 3: Проверка вычисления среднего
    def test_calculate_average_normal(self):
        """Тест вычисления среднего значения"""
        numbers = [1, 2, 3, 4, 5]
        result = self.calc.calculate_average(numbers)
        self.assertEqual(result, 3.0)
    
    def test_calculate_average_empty_list(self):
        """Тест вычисления среднего для пустого списка"""
        with self.assertRaises(ValueError) as context:
            self.calc.calculate_average([])
        self.assertEqual(str(context.exception), "Список чисел не может быть пустым")
    
    def test_calculate_average_single_number(self):
        """Тест вычисления среднего для одного числа"""
        result = self.calc.calculate_average([42])
        self.assertEqual(result, 42.0)
    
    # Тест 4: Проверка работы с файлами
    def test_read_numbers_from_file(self):
        """Тест чтения чисел из файла"""
        # Создаем тестовый файл
        with open('test_input.txt', 'w') as f:
            f.write("10\n20\n30\n")
        
        result = self.file_processor.read_numbers_from_file('test_input.txt')
        self.assertEqual(result, [10.0, 20.0, 30.0])
    
    def test_read_numbers_from_nonexistent_file(self):
        """Тест чтения из несуществующего файла"""
        with self.assertRaises(FileNotFoundError):
            self.file_processor.read_numbers_from_file('nonexistent.txt')
    
    def test_save_result_to_file(self):
        """Тест сохранения результата в файл"""
        result = self.file_processor.save_result_to_file('test_output.txt', 42.5)
        self.assertTrue(result)
        
        # Проверяем, что файл создан и содержит правильные данные
        with open('test_output.txt', 'r') as f:
            content = f.read()
        self.assertEqual(content, "42.5")

if __name__ == '__main__':
    unittest.main()