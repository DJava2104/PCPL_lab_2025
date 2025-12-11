import sys
import os

# Добавляем путь к пакету
sys.path.append(os.path.join(os.path.dirname(__file__)))

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

# Импортируем внешний пакет
try:
    from colorama import Fore, Style, init
    init(autoreset=True)  # Инициализация colorama
    COLORAMA_AVAILABLE = True
except ImportError:
    COLORAMA_AVAILABLE = False
    print("Colorama не установлен. Установите: pip install colorama")


def demonstrate_external_package():
    """Демонстрация работы внешнего пакета"""
    if COLORAMA_AVAILABLE:
        print(Fore.CYAN + Style.BRIGHT + "\nДемонстрация внешнего пакета colorama:")
        print(Fore.GREEN + "Этот текст зеленого цвета!")
        print(Fore.RED + "А этот - красного!")
        print(Fore.BLUE + "И этот - синего!")
        print(Style.RESET_ALL + "Цвет сброшен к стандартному")
    else:
        print("\nВнешний пакет colorama не установлен")


def main():
    """
    Основная функция программы
    """
    print("=" * 60)
    print("Лабораторная работа №2")
    print("Объектно-ориентированные возможности Python")
    print("=" * 60)
    
    # Номер варианта (замените на свой номер)
    N = 5  # Пример: 5-й вариант
    
    print(f"\nСоздание фигур (N = {N}):")
    print("-" * 40)
    
    # Создание объектов
    try:
        # Прямоугольник синего цвета шириной N и высотой N
        rectangle = Rectangle(N, N, "синий")
        print(rectangle)
        
        # Круг зеленого цвета радиусом N
        circle = Circle(N, "зеленый")
        print(circle)
        
        # Квадрат красного цвета со стороной N
        square = Square(N, "красный")
        print(square)
        
    except Exception as e:
        print(f"Ошибка при создании фигур: {e}")
        return
    
    # Демонстрация полиморфизма
    print(f"\n{'='*40}")
    print("Демонстрация полиморфизма:")
    print('='*40)
    
    figures = [rectangle, circle, square]
    
    for figure in figures:
        print(f"Тип фигуры: {figure.figure_type}")
        print(f"Площадь: {figure.area():.2f}")
        print(f"Цвет: {figure.color.color}")
        print("-" * 20)
    
    # Демонстрация внешнего пакета
    demonstrate_external_package()
    
    # Дополнительная информация о фигурах
    print(f"\n{'='*40}")
    print("Дополнительная информация:")
    print('='*40)
    
    print(f"\nПроверка типов:")
    print(f"rectangle является экземпляром Rectangle: {isinstance(rectangle, Rectangle)}")
    print(f"square является экземпляром Square: {isinstance(square, Square)}")
    print(f"square является экземпляром Rectangle: {isinstance(square, Rectangle)}")
    print(f"circle является экземпляром Circle: {isinstance(circle, Circle)}")


if __name__ == "__main__":
    main()