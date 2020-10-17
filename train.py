class AirBall:
    
    def __init__(self, title, price):
        self.title = title
        self.price = price
    
    def __str__(self):
        return self.title
    
    def __setattr__(self, name, value):
        if name == 'title' or name == 'price':
            super().__setattr__(name, value)
        else:
            print('Нет такого атрибута')
            raise AttributeError


# Создаем экземпляр класса
instance = AirBall('Шар большой', 150)

# Создаем новый атрибут - цвет (color)
#instance.color = 'красный'

# Выводим атрибут color
print(instance)


class Animal:
    def __init__(self):
        print('Это животное (' + self.__class__.__name__ + ')')


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print('У собаки 4 лапы (' + self.__class__.__name__ + ')')        


dog_instance = Dog()


class Person:    
    
    def __init__(self, name, age):
        if Person.check_age(age):
            self.name = name
            self.age = age
        else:
            raise ValueError
    
    @staticmethod
    def check_age(age):
        return age > 0

    
# Создаем экземпляр класса Person
# Создаем экземпляр класса Person (здесь срабатывает конструктор __int__, в котором стоит проверка возраста)
instance = Person('Василий', 35)

# Здесь конструктор уже не срабатывает
instance.age = -35
print(instance.age) # -35


class Person:
    def __init__(self, name, age):
        if Person.check_age(age):
            self.name = name
            self.__age = age
        else:
            raise ValueError
    
    @staticmethod
    def check_age(age):
        return age > 0

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        if Person.check_age(age):
            self.__age = age
        else:
            raise ValueError   
    

instance = Person('Василий', 35)

# На этой строке получаем ошибку, потому что сработала проверка в сеттере
instance.age = 20
print(instance.age)


class Question():

    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer


question_list = [Question('Сколько будет 2+2?', '4'),
                 Question('Сколько будет 3 в квадрате?', '9'),
                 Question('Сколько будет 2+2*2?', '6')]


for question_instance in question_list:
    
    # Обращаемся к атрибуту - text
    print(question_instance.text)

    # Просим пользователя ввести значение и запоминаем его в переменной user_answer
    user_answer = input('Ваш ответ: ')

    # Вызываем метод check_answer у экземпляра question
    # Метод check_answer возвращает либо True либо False
    if question_instance.check_answer(user_answer):
        print('Правильно')
    else:
        print('Не правильно')

class Question():

    score = 10 # Добавили атрибут класса

    def __init__(self, text, correct_answer):
        self.text = text
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer


question_list = [Question('Сколько будет 2+2?', '4'),
                 Question('Сколько будет 3 в квадрате?', '9'),
                 Question('Сколько будет 2+2*2?', '6')]

total_score = 0

for question_instance in question_list:
    
    # Обращаемся к атрибуту - text
    print(question_instance.text)

    # Просим пользователя ввести значение и запоминаем его в переменной user_answer
    user_answer = input('Ваш ответ: ')

    # Вызываем метод check_answer у экземпляра question
    # Метод check_answer возвращает либо True либо False
    if question_instance.check_answer(user_answer):
        total_score += Question.score # Обращаемся к атрибуту класса score через класс Question

print(f'Вы набрали {total_score} баллов')
