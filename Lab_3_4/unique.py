class Unique(object):
    """
    Итератор для удаления дубликатов
    """
    def __init__(self, items, **kwargs):
        """
        Args:
            items: массив или генератор
            **kwargs: может содержать ignore_case (bool)
        """
        self.items = iter(items)
        self.seen = set()
        self.ignore_case = kwargs.get('ignore_case', False)
    
    def __next__(self):
        while True:
            item = next(self.items)
            
            # Обработка в зависимости от ignore_case
            if self.ignore_case and isinstance(item, str):
                check_item = item.lower()
            else:
                check_item = item
            
            # Если элемент еще не встречался
            if check_item not in self.seen:
                self.seen.add(check_item)
                return item
    
    def __iter__(self):
        return self


if __name__ == "__main__":
    print("Тест 1 - числа с дубликатами:")
    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    for item in Unique(data1):
        print(item, end=" ")
    print()
    
    print("\nТест 2 - строки без ignore_case:")
    data2 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    for item in Unique(data2):
        print(item, end=" ")
    print()
    
    print("\nТест 3 - строки с ignore_case=True:")
    for item in Unique(data2, ignore_case=True):
        print(item, end=" ")
    print()