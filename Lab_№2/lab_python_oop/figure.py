from abc import ABC, abstractmethod

class GeometricFigure(ABC):
    """
    Абстрактный класс 'Геометрическая фигура'
    """
    
    @property
    @abstractmethod
    def figure_type(self):
        """Абстрактное свойство для получения типа фигуры"""
        pass
    
    @abstractmethod
    def area(self):
        """Абстрактный метод для вычисления площади фигуры"""
        pass
    
    def __repr__(self):
        """Метод для строкового представления фигуры"""
        return "{} {} цвета площадью {:.2f}".format(
            self.figure_type,
            self.color.color,
            self.area()
        )