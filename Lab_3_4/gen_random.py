import random

def gen_random(num_count, begin, end):
    """
    Генератор случайных чисел в заданном диапазоне
    
    Args:
        num_count: количество чисел
        begin: начало диапазона
        end: конец диапазона
    
    Yields:
        Случайные целые числа в диапазоне [begin, end]
    """
    for _ in range(num_count):
        yield random.randint(begin, end)


if __name__ == "__main__":
    print("Тест 1 - 5 чисел от 1 до 3:")
    for num in gen_random(5, 1, 3):
        print(num, end=" ")
    print()
    
    print("\nТест 2 - 3 числа от 10 до 20:")
    print(list(gen_random(3, 10, 20)))