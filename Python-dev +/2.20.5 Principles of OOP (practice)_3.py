class Human:
    def __init__(self, name: str):
        self.name: str = name

    # ответ по умолчанию для всех одинаковый, можно
    # доверить его родительскому классу
    def answer_question(self, question: str):
        if question:
            return 'Очень интересный вопрос! Не знаю.'
        return 'Unexpected Error'


class Student(Human):
    #  метод ask_question() принимает параметр someone:
    #  это объект, экземпляр класса Curator, Mentor или CodeReviewer,
    #  которому Student задаёт вопрос;
    #  параметр question — это просто строка
    #  имя объекта и текст вопроса задаются при вызове метода ask_question
    def ask_question(self, someone: Human, question: str):
        # напечатайте на экран вопрос в нужном формате
        print(f'{someone.name}, {question}')
        # запросите ответ на вопрос у someone
        ask: str = someone.answer_question(question)
        print(ask)

        print()  # этот print выводит разделительную пустую строку


class Curator(Human):
    def __init__(self, name: str):
        super().__init__(name)
        self.questions: dict = {
            'мне грустненько, что делать?': (
                'Держись, всё получится. ' 'Хочешь видео с котиками?'
            ),
        }

    def answer_question(self, question: str):
        # здесь нужно проверить, пришёл куратору знакомый вопрос или нет
        # если да - ответить на него
        # если нет - вызвать метод answer_question() у родительского класса
        if question in self.questions:
            return self.questions[question]
        return super().answer_question(question)


# объявите и реализуйте классы CodeReviewer и Mentor
class CodeReviewer(Human):
    def __init__(self, name: str):
        super().__init__(name)
        self.questions: dict = {
            'что не так с моим проектом?': 'О, вопрос про проект, это я люблю.'
        }

    def answer_question(self, question: str):
        if question in self.questions:
            return self.questions[question]
        return super().answer_question(question)


class Mentor(Human):
    def __init__(self, name: str):
        super().__init__(name)
        self.questions: dict = {
            'как устроиться работать питонистом?': 'Сейчас расскажу.',
            'мне грустненько, что делать?': (
                'Отдохни и возвращайся с вопросами по теории.'
            ),
        }

    def answer_question(self, question: str):
        if question in self.questions:
            return self.questions[question]
        return super().answer_question(question)


# следующий код менять не нужно, он работает, мы проверяли
student1 = Student('Тимофей')
curator = Curator('Марина')
mentor = Mentor('Ира')
reviewer = CodeReviewer('Евгений')
friend = Human('Виталя')

student1.ask_question(curator, 'мне грустненько, что делать?')
student1.ask_question(mentor, 'мне грустненько, что делать?')
student1.ask_question(reviewer, 'когда каникулы?')
student1.ask_question(reviewer, 'что не так с моим проектом?')
student1.ask_question(friend, 'как устроиться на работу питонистом?')
student1.ask_question(mentor, 'как устроиться работать питонистом?')
