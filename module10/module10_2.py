import threading
import time

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies = 100 # Начальное количество врагов

    def fight(self):
        days = 0
        while self.enemies > 0:
            print(f'{self.name} сражается {days} дней..., осталось {self.enemies} врагов.')
            self.enemies -= self.power
            time.sleep(1)
            days += 1

        print(f'{self.name} одержал победу спустя {days} дней!')

    def run(self):
        print(f'{self.name}, на нас напали!')
        self.fight()

# Создаем и запускаем 2 потока на основе класса Knight
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()

# Подождем завершения обоих потоков
first_knight.join()
second_knight.join()

# Распечатываем сообщение об окончании боя
print('Битва окончена!')