#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Модульные тесты для геометрических фигур
"""

import unittest
import sys
import os

# Добавляем путь к пакету
sys.path.append(os.path.join(os.path.dirname(__file__), 'lab_python_oop'))

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square


class TestGeometricFigures(unittest.TestCase):
    """Тесты для геометрических фигур"""
    
    def test_rectangle_creation(self):
        """Тест создания прямоугольника"""
        rect = Rectangle(5, 3, "синий")
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 3)
        self.assertEqual(rect.color.color, "синий")
    
    def test_rectangle_area(self):
        """Тест вычисления площади прямоугольника"""
        rect = Rectangle(4, 6, "красный")
        self.assertEqual(rect.area(), 24)
    
    def test_circle_creation(self):
        """Тест создания круга"""
        circle = Circle(5, "зеленый")
        self.assertEqual(circle.radius, 5)
        self.assertEqual(circle.color.color, "зеленый")
    
    def test_circle_area(self):
        """Тест вычисления площади круга"""
        circle = Circle(2, "желтый")
        expected_area = 3.141592653589793 * 4  # π * r²
        self.assertAlmostEqual(circle.area(), expected_area)
    
    def test_square_creation(self):
        """Тест создания квадрата"""
        square = Square(4, "красный")
        self.assertEqual(square.width, 4)
        self.assertEqual(square.height, 4)
        self.assertEqual(square.color.color, "красный")
    
    def test_square_area(self):
        """Тест вычисления площади квадрата"""
        square = Square(5, "синий")
        self.assertEqual(square.area(), 25)
    
    def test_figure_types(self):
        """Тест типов фигур"""
        rect = Rectangle(1, 2, "белый")
        circle = Circle(1, "черный")
        square = Square(1, "серый")
        
        self.assertEqual(rect.figure_type, "Прямоугольник")
        self.assertEqual(circle.figure_type, "Круг")
        self.assertEqual(square.figure_type, "Квадрат")
    
    def test_inheritance(self):
        """Тест наследования"""
        square = Square(1, "красный")
        self.assertIsInstance(square, Rectangle)
    
    def test_color_validation(self):
        """Тест валидации цвета"""
        rect = Rectangle(1, 1, "синий")
        
        with self.assertRaises(ValueError):
            rect.color.color = ""  # Пустой цвет
        
        with self.assertRaises(ValueError):
            rect.color.color = None  # None цвет


if __name__ == '__main__':
    unittest.main()