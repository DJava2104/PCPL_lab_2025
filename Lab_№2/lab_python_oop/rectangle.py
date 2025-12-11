from .figure import GeometricFigure
from .color import FigureColor

class Rectangle(GeometricFigure):
    """
    Класс 'Прямоугольник'
    """
    
    figure_type = "Прямоугольник"
    
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor()
        self.color.color = color
    
    def area(self):
        """Вычисление площади прямоугольника"""
        return self.width * self.height
    
    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {}. Площадь: {:.2f}".format(
            self.figure_type,
            self.color.color,
            self.width,
            self.height,
            self.area()
        )