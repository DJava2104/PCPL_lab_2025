import math
from .figure import GeometricFigure
from .color import FigureColor

class Circle(GeometricFigure):
    """
    Класс 'Круг'
    """
    
    figure_type = "Круг"
    
    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor()
        self.color.color = color
    
    def area(self):
        """Вычисление площади круга"""
        return math.pi * self.radius ** 2
    
    def __repr__(self):
        return "{} {} цвета радиусом {}. Площадь: {:.2f}".format(
            self.figure_type,
            self.color.color,
            self.radius,
            self.area()
        )