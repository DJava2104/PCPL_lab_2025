# lab1_oop.py
import sys
import math

class CoefficientValidator:
    """Класс для валидации коэффициентов"""
    
    @staticmethod
    def is_valid_float(value):
        """Проверка, можно ли преобразовать строку в действительное число."""
        try:
            float(value)
            return True
        except ValueError:
            return False

class CoefficientInput:
    """Класс для ввода коэффициентов"""
    
    def __init__(self, prompt, param_value=None):
        self.prompt = prompt
        self.param_value = param_value
        self.validator = CoefficientValidator()
    
    def get_value(self):
        """
        Получение корректного коэффициента.
        Если параметр задан и корректен, используем его.
        Иначе запрашиваем с клавиатуры.
        """
        if self.param_value is not None and self.validator.is_valid_float(self.param_value):
            value = float(self.param_value)
            print(f"{self.prompt}: {value} (из параметров)")
            return value
        
        while True:
            try:
                value = input(f"{self.prompt}: ")
                if self.validator.is_valid_float(value):
                    return float(value)
                else:
                    print("Ошибка: введите действительное число")
            except KeyboardInterrupt:
                print("\nПрограмма прервана пользователем")
                sys.exit(0)

class BiquadraticEquation:
    """Класс для решения биквадратного уравнения"""
    
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.real_roots = []
    
    def solve(self):
        """Решение биквадратного уравнения ax^4 + bx^2 + c = 0"""
        print(f"\nУравнение: {self.a}x^4 + {self.b}x^2 + {self.c} = 0")
        
        # Проверка коэффициента a
        if self.a == 0:
            print("Ошибка: коэффициент A не может быть равен 0 для биквадратного уравнения")
            return self.real_roots
        
        # Решаем квадратное уравнение относительно t = x^2
        D = self.b**2 - 4*self.a*self.c
        print(f"Дискриминант: {D}")
        
        if D < 0:
            print("Действительных корней нет")
        elif D == 0:
            self._handle_zero_discriminant()
        else:  # D > 0
            self._handle_positive_discriminant()
        
        # Убираем возможные дубликаты и сортируем
        self.real_roots = sorted(list(set(round(r, 10) for r in self.real_roots)))
        
        if self.real_roots:
            print(f"\nВсе действительные корни: {self.real_roots}")
        else:
            print("\nДействительных корней нет")
        
        return self.real_roots
    
    def _handle_zero_discriminant(self):
        """Обработка случая D = 0"""
        t = -self.b / (2*self.a)
        print(f"t = x^2 = {t}")
        
        if t > 0:
            x1 = math.sqrt(t)
            x2 = -math.sqrt(t)
            self.real_roots.extend([x1, x2])
            print(f"Корни: x1 = {x1}, x2 = {x2}")
        elif t == 0:
            x = 0
            self.real_roots.append(x)
            print(f"Корень: x = {x}")
        else:
            print("Действительных корней нет")
    
    def _handle_positive_discriminant(self):
        """Обработка случая D > 0"""
        D = self.b**2 - 4*self.a*self.c
        t1 = (-self.b + math.sqrt(D)) / (2*self.a)
        t2 = (-self.b - math.sqrt(D)) / (2*self.a)
        print(f"t1 = x^2 = {t1}, t2 = x^2 = {t2}")
        
        # Обрабатываем t1
        self._process_t(t1, "t1")
        
        # Обрабатываем t2
        self._process_t(t2, "t2")
    
    def _process_t(self, t, t_name):
        """Обработка значения t = x^2"""
        if t > 0:
            x1 = math.sqrt(t)
            x2 = -math.sqrt(t)
            self.real_roots.extend([x1, x2])
            print(f"Корни из {t_name}: x1 = {x1}, x2 = {x2}")
        elif t == 0:
            # Проверяем, чтобы не дублировать корень x=0
            if 0 not in self.real_roots:
                x = 0
                self.real_roots.append(x)
                print(f"Корень из {t_name}: x = {x}")

class BiquadraticSolverApp:
    """Основной класс приложения"""
    
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None
    
    def parse_command_line_args(self):
        """Парсинг параметров командной строки"""
        a_param = b_param = c_param = None
        
        if len(sys.argv) >= 2:
            a_param = sys.argv[1]
        if len(sys.argv) >= 3:
            b_param = sys.argv[2]
        if len(sys.argv) >= 4:
            c_param = sys.argv[3]
        
        return a_param, b_param, c_param
    
    def get_coefficients(self):
        """Получение всех коэффициентов"""
        a_param, b_param, c_param = self.parse_command_line_args()
        
        print("\nВведите коэффициенты (A, B, C):")
        a_input = CoefficientInput("A", a_param)
        b_input = CoefficientInput("B", b_param)
        c_input = CoefficientInput("C", c_param)
        
        self.a = a_input.get_value()
        self.b = b_input.get_value()
        self.c = c_input.get_value()
    
    def run(self):
        """Основной метод запуска приложения"""
        print("=" * 50)
        print("Решение биквадратного уравнения Ax^4 + Bx^2 + C = 0")
        print("=" * 50)
        
        self.get_coefficients()
        
        equation = BiquadraticEquation(self.a, self.b, self.c)
        equation.solve()

def main():
    app = BiquadraticSolverApp()
    app.run()

if __name__ == "__main__":
    main()