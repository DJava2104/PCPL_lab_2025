from .rectangle import Rectangle

class Square(Rectangle):
    """
    Класс 'Квадрат' (наследуется от Прямоугольника)
    """
    
    figure_type = "Квадрат"
    
    def __init__(self, side, color):
        # Вызываем конструктор родительского класса
        super().__init__(side, side, color)
    
    def __repr__(self):
        return "{} {} цвета со стороной {}. Площадь: {:.2f}".format(
            self.figure_type,
            self.color.color,
            self.width,
            self.area()
        )