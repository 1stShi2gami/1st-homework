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

    def __len__(self):
        return self.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name

    def __bool__(self):
        return bool(self.age)
    def __del__(self):
        print(f'{self.name} ушёл')


tim = Human('Timur', 30)
tan = Human("Tanya", 30)
