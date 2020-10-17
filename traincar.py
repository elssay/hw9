class Car:
    def __init__(self, title, power):
        self.title = title
        self.power = power
    
    def get_price(self):
        return self.power * 1000


class Person:
    def __init__(self, name, car):
        self.name = name
        self.car = car


# Создаем экземпляр класса Car
instance_car = Car('Лада', 200)

# Создаем экземпляр класса Person и передаем во второй параметр экземпляр instance_car
instance_person = Person('Василий', instance_car)

# Теперь у instance_person в атрибуте car находится instance_car, а значит мы можем обращаться через точку к его методам
print(instance_person.car.get_price())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Diploma:    
    def __init__(self, results):
        self.results = results

    def get_average_score(self):
        total_score = 0
        for result in self.results:
            total_score += result['score']
        return total_score / len(self.results)

class Student(Person):

    def __init__(self, name, age, diploma):
        super().__init__(name, age)
        self.diploma = diploma
    
    def get_average_score(self):
        return self.diploma.get_average_score()

class Professor(Person):

    def __init__(self, name, age, sudents):
        super().__init__(name, age)
        self.sudents = sudents
    
    def get_average_score(self):
        total_score = 0
        for sudent in self.sudents:
            total_score += sudent.get_average_score()
        return total_score / len(self.sudents)

# Создаем список результатов для каждого предмета.
# Для простоты эксперемента# Для простоты эксперимента каждому предмету поставим оценку 4
STUDENT_SUBJECTS = ['math', 'history', 'english']
results = []
for subject in STUDENT_SUBJECTS:
    results.append({'subject': subject, 'score': 4})

# Создаем экземпляр класса Student
student1 = Student('Иван', 20, Diploma(results))

# Повторяем процедуру еще для 2 студентов
results = []
for subject in STUDENT_SUBJECTS:
    results.append({'subject': subject, 'score': 5})
student2 = Student('Юля', 21, Diploma(results))

results = []
for subject in STUDENT_SUBJECTS:
    results.append({'subject': subject, 'score': 4})
student3 = Student('Игорь', 22, Diploma(results))

# Создаем экземпляр класса Student
professor1 = Professor('Сергей Сергеевич', 47, [student1, student2])

# Считаем средний балл по всем студентам для профессора
print(professor1.get_average_score())

professor2 = Professor('Петр Петрович', 48, [student1, student3])
print(professor2.get_average_score())
print(student1.diploma.get_average_score())