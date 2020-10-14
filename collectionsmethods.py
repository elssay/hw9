from collections import defaultdict, Counter


sales_log = [{'user': 'Маша', 'item': 'Телескоп'},
       {'user': 'Юля', 'item': 'Айфон'}, 
       {'user': 'Иван', 'item': 'Ноутбук'},
       {'user': 'Сергей', 'item': 'Браслет'},
       {'user': 'Инна', 'item': 'Айфон'},
       {'user': 'Ольга', 'item': 'Айфон'},
       {'user': 'Дмитрий', 'item': 'Браслет'}, ]

sales_dict = defaultdict(int) # Создаем словарь с заранее заданным типом значений

for element in sales_log:
    # Добавляем элемент в словарь sales_dict
    # element['item'] - название товара
    # Если ключа с таким названием в sales_dict нет, то будет значение 0,
    # таким образом мы просто увеличим его на 1  
    sales_dict[element['item']] += 1
print(sales_dict)
sales_counter = Counter(sales_dict) # Создаем объект Counter из полученного словаря и используем метод most_common
print(f'Самый популярный товар: {sales_counter.most_common(1)[0][0]}. Количество продаж: {sales_counter.most_common(1)[0][1]}')