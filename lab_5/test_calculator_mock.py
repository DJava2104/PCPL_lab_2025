"""
Тесты с использованием Mock-объектов
"""
import unittest
from unittest.mock import Mock, patch, mock_open, MagicMock
from calculator import Calculator, FileProcessor

class TestCalculatorMock(unittest.TestCase):
    """Тесты с Mock-объектами"""
    
    def setUp(self):
        self.calc = Calculator()
        self.file_processor = FileProcessor()
    
    # Тест с Mock для сложения
    def test_add_with_mock(self):
        """Тест сложения с использованием Mock"""
        # Создаем mock-объект для сложения
        mock_add = Mock(return_value=10)
        
        # Заменяем метод add калькулятора на mock
        original_add = self.calc.add
        self.calc.add = mock_add
        
        # Вызываем метод
        result = self.calc.add(5, 5)
        
        # Проверяем, что mock был вызван с правильными аргументами
        mock_add.assert_called_once_with(5, 5)
        
        # Проверяем результат
        self.assertEqual(result, 10)
        
        # Восстанавливаем оригинальный метод
        self.calc.add = original_add
    
    # Тест с patch для работы с файлами
    @patch('calculator.open', new_callable=mock_open, read_data="10\n20\n30\n")
    def test_read_numbers_with_mock_file(self, mock_file):
        """Тест чтения чисел с mock-файлом"""
        result = self.file_processor.read_numbers_from_file('any_file.txt')
        
        # Проверяем, что файл был открыт для чтения
        mock_file.assert_called_once_with('any_file.txt', 'r')
        
        # Проверяем результат
        self.assertEqual(result, [10.0, 20.0, 30.0])
    
    # Тест с MagicMock для сложной логики
    def test_calculate_average_with_magic_mock(self):
        """Тест вычисления среднего с MagicMock"""
        # Создаем MagicMock для списка чисел
        mock_numbers = MagicMock()
        mock_numbers.__len__.return_value = 3
        
        # Настраиваем поведение sum для нашего mock-объекта
        with patch('builtins.sum', return_value=30) as mock_sum:
            # Вызываем метод
            result = self.calc.calculate_average(mock_numbers)
            
            # Проверяем вызовы
            mock_sum.assert_called_once_with(mock_numbers)
            
            # Проверяем результат (30 / 3 = 10)
            self.assertEqual(result, 10)
    
    # Тест с side_effect
    def test_divide_with_side_effect(self):
        """Тест деления с side_effect"""
        # Создаем mock с side_effect
        mock_divide = Mock(side_effect=lambda x, y: x / y if y != 0 else ValueError("Деление на ноль"))
        
        # Заменяем метод
        original_divide = self.calc.divide
        self.calc.divide = mock_divide
        
        # Тестируем нормальное деление
        result = self.calc.divide(10, 2)
        self.assertEqual(result, 5)
        
        # Тестируем деление на ноль
        result = self.calc.divide(10, 0)
        self.assertIsInstance(result, ValueError)
        
        # Восстанавливаем оригинальный метод
        self.calc.divide = original_divide
    
    # Интеграционный тест с patch
    @patch('calculator.FileProcessor.read_numbers_from_file')
    def test_integration_with_mock(self, mock_read):
        """Интеграционный тест с mock для чтения файла"""
        # Настраиваем mock для возвращения тестовых данных
        mock_read.return_value = [1.0, 2.0, 3.0, 4.0, 5.0]
        
        # Читаем "файл"
        numbers = self.file_processor.read_numbers_from_file('test.txt')
        
        # Вычисляем среднее
        result = self.calc.calculate_average(numbers)
        
        # Проверяем результат
        self.assertEqual(result, 3.0)
        
        # Проверяем, что mock был вызван
        mock_read.assert_called_once_with('test.txt')

if __name__ == '__main__':
    unittest.main()