"""
Калькулятор для выполнения математических операций
"""
import math

class Calculator:
    """Класс калькулятора с базовыми математическими операциями"""
    
    def add(self, a, b):
        """Сложение двух чисел"""
        return a + b
    
    def subtract(self, a, b):
        """Вычитание"""
        return a - b
    
    def multiply(self, a, b):
        """Умножение"""
        return a * b
    
    def divide(self, a, b):
        """Деление с проверкой деления на ноль"""
        if b == 0:
            raise ValueError("Деление на ноль невозможно")
        return a / b
    
    def power(self, a, b):
        """Возведение в степень"""
        return a ** b
    
    def square_root(self, a):
        """Квадратный корень с проверкой отрицательного числа"""
        if a < 0:
            raise ValueError("Квадратный корень из отрицательного числа невозможен")
        return math.sqrt(a)
    
    def calculate_average(self, numbers):
        """Вычисление среднего значения списка чисел"""
        if not numbers:
            raise ValueError("Список чисел не может быть пустым")
        return sum(numbers) / len(numbers)


# Функция для работы с файлами (для демонстрации Mock-объектов)
class FileProcessor:
    """Класс для обработки файлов"""
    
    def read_numbers_from_file(self, filename):
        """Чтение чисел из файла"""
        try:
            with open(filename, 'r') as file:
                numbers = [float(line.strip()) for line in file if line.strip()]
            return numbers
        except FileNotFoundError:
            raise FileNotFoundError(f"Файл {filename} не найден")
        except ValueError:
            raise ValueError("Файл содержит некорректные данные")
    
    def save_result_to_file(self, filename, result):
        """Сохранение результата в файл"""
        with open(filename, 'w') as file:
            file.write(str(result))
        return True