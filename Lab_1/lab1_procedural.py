# lab1_procedural.py
import sys
import math

def is_valid_float(value):
    """Проверка, можно ли преобразовать строку в действительное число."""
    try:
        float(value)
        return True
    except ValueError:
        return False

def get_coefficient(prompt, param_value=None):
    """
    Получение корректного коэффициента.
    Если параметр задан и корректен, используем его.
    Иначе запрашиваем с клавиатуры.
    """
    if param_value is not None and is_valid_float(param_value):
        value = float(param_value)
        print(f"{prompt}: {value} (из параметров)")
        return value
    
    while True:
        try:
            value = input(f"{prompt}: ")
            if is_valid_float(value):
                return float(value)
            else:
                print("Ошибка: введите действительное число")
        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем")
            sys.exit(0)

def solve_biquadratic(a, b, c):
    """Решение биквадратного уравнения ax^4 + bx^2 + c = 0"""
    print(f"\nУравнение: {a}x^4 + {b}x^2 + {c} = 0")
    
    # Проверка коэффициента a
    if a == 0:
        print("Ошибка: коэффициент A не может быть равен 0 для биквадратного уравнения")
        return []
    
    # Решаем квадратное уравнение относительно t = x^2
    D = b**2 - 4*a*c
    print(f"Дискриминант: {D}")
    
    real_roots = []
    
    if D < 0:
        print("Действительных корней нет")
    elif D == 0:
        t = -b / (2*a)
        print(f"t = x^2 = {t}")
        if t > 0:
            x1 = math.sqrt(t)
            x2 = -math.sqrt(t)
            real_roots.extend([x1, x2])
            print(f"Корни: x1 = {x1}, x2 = {x2}")
        elif t == 0:
            x = 0
            real_roots.append(x)
            print(f"Корень: x = {x}")
        else:
            print("Действительных корней нет")
    else:  # D > 0
        t1 = (-b + math.sqrt(D)) / (2*a)
        t2 = (-b - math.sqrt(D)) / (2*a)
        print(f"t1 = x^2 = {t1}, t2 = x^2 = {t2}")
        
        # Обрабатываем t1
        if t1 > 0:
            x1 = math.sqrt(t1)
            x2 = -math.sqrt(t1)
            real_roots.extend([x1, x2])
            print(f"Корни из t1: x1 = {x1}, x2 = {x2}")
        elif t1 == 0:
            x = 0
            real_roots.append(x)
            print(f"Корень из t1: x = {x}")
        
        # Обрабатываем t2
        if t2 > 0:
            x3 = math.sqrt(t2)
            x4 = -math.sqrt(t2)
            real_roots.extend([x3, x4])
            print(f"Корни из t2: x3 = {x3}, x4 = {x4}")
        elif t2 == 0 and t1 != 0:  # чтобы не дублировать корень x=0
            x = 0
            real_roots.append(x)
            print(f"Корень из t2: x = {x}")
    
    # Убираем возможные дубликаты и сортируем
    real_roots = sorted(list(set(round(r, 10) for r in real_roots)))
    
    if real_roots:
        print(f"\nВсе действительные корни: {real_roots}")
    else:
        print("\nДействительных корней нет")
    
    return real_roots

def main():
    print("=" * 50)
    print("Решение биквадратного уравнения Ax^4 + Bx^2 + C = 0")
    print("=" * 50)
    
    # Парсинг параметров командной строки
    a_param = b_param = c_param = None
    
    if len(sys.argv) >= 2:
        a_param = sys.argv[1]
    if len(sys.argv) >= 3:
        b_param = sys.argv[2]
    if len(sys.argv) >= 4:
        c_param = sys.argv[3]
    
    # Получение коэффициентов
    print("\nВведите коэффициенты (A, B, C):")
    a = get_coefficient("A", a_param)
    b = get_coefficient("B", b_param)
    c = get_coefficient("C", c_param)
    
    # Решение уравнения
    solve_biquadratic(a, b, c)

if __name__ == "__main__":
    main()