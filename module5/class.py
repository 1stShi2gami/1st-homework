class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_INFO()
    def say_INFO(self):
        print(f'Привет, меня зовут: {self.name}, мне: {self.age}')

    def birtheday(self):
        self.age += 1
        print(f'Поздравляю с Днем Рождения! Теперь мне: {self.age}')


tim = Human('Timur', 31)
tan = Human("Tanya", 26)

tim.birtheday()