def field(items, *args):
    """
    Генератор для извлечения полей из словарей
    
    Args:
        items: список словарей
        *args: имена полей для извлечения
    
    Yields:
        Если передан один аргумент - значения поля
        Если несколько аргументов - словари с указанными полями
    """
    assert len(args) > 0, "Нужно указать хотя бы одно поле"
    
    if len(args) == 1:
        # Если одно поле - возвращаем только значения
        field_name = args[0]
        for item in items:
            if field_name in item and item[field_name] is not None:
                yield item[field_name]
    else:
        # Если несколько полей - возвращаем словари
        for item in items:
            result = {}
            has_data = False
            for field_name in args:
                if field_name in item and item[field_name] is not None:
                    result[field_name] = item[field_name]
                    has_data = True
            if has_data:
                yield result


if __name__ == "__main__":
    # Тестовые данные
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': None, 'price': 1500},
        {'price': 3000}
    ]
    
    print("Тест 1 - одно поле 'title':")
    for item in field(goods, 'title'):
        print(item)
    
    print("\nТест 2 - два поля 'title', 'price':")
    for item in field(goods, 'title', 'price'):
        print(item)