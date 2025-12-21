"""
BDD тесты с использованием behave
"""
from behave import given, when, then
from calculator import Calculator

@given('я создаю новый калькулятор')
def step_create_calculator(context):
    """Создание калькулятора"""
    context.calculator = Calculator()

@given('у меня есть числа {num1:d} и {num2:d}')
def step_given_numbers(context, num1, num2):
    """Задание чисел для операций"""
    context.num1 = num1
    context.num2 = num2

@given('у меня есть список чисел')
def step_given_list_of_numbers(context):
    """Задание списка чисел"""
    context.numbers = [float(row['number']) for row in context.table]

@when('я складываю эти числа')
def step_add_numbers(context):
    """Выполнение сложения"""
    context.result = context.calculator.add(context.num1, context.num2)

@when('я вычитаю второе число из первого')
def step_subtract_numbers(context):
    """Выполнение вычитания"""
    context.result = context.calculator.subtract(context.num1, context.num2)

@when('я умножаю эти числа')
def step_multiply_numbers(context):
    """Выполнение умножения"""
    context.result = context.calculator.multiply(context.num1, context.num2)

@when('я делю первое число на второе')
def step_divide_numbers(context):
    """Выполнение деления"""
    try:
        context.result = context.calculator.divide(context.num1, context.num2)
    except Exception as e:
        context.exception = e

@when('я вычисляю среднее значение этих чисел')
def step_calculate_average(context):
    """Вычисление среднего значения"""
    try:
        context.result = context.calculator.calculate_average(context.numbers)
    except Exception as e:
        context.exception = e

@then('результат должен быть {expected_result:d}')
def step_check_result_int(context, expected_result):
    """Проверка целочисленного результата"""
    assert context.result == expected_result, \
        f"Ожидалось {expected_result}, получено {context.result}"

@then('результат должен быть {expected_result:f}')
def step_check_result_float(context, expected_result):
    """Проверка результата с плавающей точкой"""
    assert abs(context.result - expected_result) < 0.0001, \
        f"Ожидалось {expected_result}, получено {context.result}"

@then('я должен получить ошибку деления на ноль')
def step_check_division_by_zero_error(context):
    """Проверка ошибки деления на ноль"""
    assert hasattr(context, 'exception'), "Ожидалась ошибка, но её не было"
    assert isinstance(context.exception, ValueError)
    assert str(context.exception) == "Деление на ноль невозможно"

@then('я должен получить ошибку пустого списка')
def step_check_empty_list_error(context):
    """Проверка ошибки пустого списка"""
    assert hasattr(context, 'exception'), "Ожидалась ошибка, но её не было"
    assert isinstance(context.exception, ValueError)
    assert str(context.exception) == "Список чисел не может быть пустым"