class AirBall:
    
    def __init__(self, title, price):
        self.title = title
        self.price = price


# Создаем объекты класса AirBall
item1 = AirBall('Красный шарик', 200)
item2 = AirBall('Синий шарик', 120)
item3 = AirBall('Черный шарик', 100)
item4 = AirBall('Зеленый гелиевый шарик', 4500)

print(item1.price)

class AirBall():
    
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    # Определяем метод класса. Первый параметр любого метода - это self
    def get_promo_price(self, discount):
        
        # Обращаемся к атрибутам экземпляра класса через self.
        return self.price - self.price * discount / 100


# Создаем экземпляр класса
item_air_bal = AirBall('Красный шарик', 80)

# Обращаемся к методу get_promo_price класса AirBall
print(f'Промо цена: {item_air_bal.get_promo_price(50)}')

class AirBall:
    
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def __str__(self):
        return f'{self.title} цена: {self.price}'


instance = AirBall('Шар большой', 150)

print(instance)
#Результат:

#Шар большой цена: 150
#Обычно в методе __str__ возвращают название экземпляра.

#Любой код, который получает строку - вызовет метод __str__. Этот код тоже вызовет метод __str__:

instance = AirBall('Шар большой', 150)

new_string = str(instance) + ' [новая часть строки]'

print(new_string)

class Employee:
    
    def __init__(self, salary):
        self.salary = salary
    
    
    def get_tax(self):
        return self.salary * 0.3


employee1 = Employee(100)
employee2 = Employee(200)

print(f'Подоходный налог сотрудника 1: {employee1.get_tax()}')
print(f'Подоходный налог сотрудника 2: {employee2.get_tax()}')