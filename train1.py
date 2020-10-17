class Question():

    score = 10

    def __init__(self, text, correct_answer):
        if Question.check_text(text):
            self.__text = text
            self.correct_answer = correct_answer
        else:
            raise ValueError

    def check_answer(self, user_answer):
        return user_answer == self.correct_answer
    
    @staticmethod
    def check_text(text):
        if text:
            return True
        else:
            return False

    @property
    def text(self):
        return self.__text

    @text.setter
    def text(self, text):
        if Question.check_text(text):
            self.__text = text
        else:
            raise ValueError


question_list = []

total_score = 0

for i in range(2):
    # Пользователь вводит текст вопроса и правильный ответ
    text = input('Введите текст вопроса: ')
    correct_answer = input('Введите правильный ответ: ')

    # Создаем экземпляр класса
    question_instance = Question(text, correct_answer)

    # Спрашиваем хочет ли  пользователь подкорректировать текст вопроса
    i_want_change = input('Вы хотите изменить текст вопроса? (1-да, 0-нет): ')
    if i_want_change == '1':
        
        # Если хочет - вводим новый текст
        text = input('Введите новый текст вопроса: ')

        # Обновляем атрибут text у экземпляра класса
        question_instance.text = text
    
    # Добавляемм экземпляр класса в список вопросов
    question_list.append(question_instance)

print('----------')
print('Викторина НАЧАЛАСЬ!')
print('----------')

for question_instance in question_list:
    
    # Обращаемся к атрибуту - text
    print(question_instance.text)

    # Просим пользователя ввести значение и запоминаем его в переменной user_answer
    user_answer = input('Ваш ответ: ')

    # Вызываем метод check_answer у экземпляра question
    # Метод check_answer возвращает либо True либо False
    if question_instance.check_answer(user_answer):
        # Увеличиваем total_score, обращаясь к атрибуту класса score через класс Question
        total_score += Question.score

print(f'Вы набрали {total_score} баллов')