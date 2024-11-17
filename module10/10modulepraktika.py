import random
import time
from itertools import count
from threading import Thread
import queue


class Bulka(Thread):

    def __init__(self, queue):
        self.queue = queue
        super().__init__()

    def run(self):
        while True:
            time.sleep(random.randint(1, 3))
            if random.random() > 0.9:
                self.queue.put('Bulka podgorela')
            else:
                self.queue.put('Bulka normalnaya')


class Kotleta(Thread):
    def __init__(self, queue, count):
        self.count = count
        self.queue = queue
        super().__init__()

    def run(self):

        while self.count:
            print(self.queue.qsize())
            bulka = self.queue.get()
            if bulka == 'Bulka normalnaya':
                time.sleep(random.randint(1, 3))
                self.count -= 1
            print('buulok k prigotovleniyu ostalos', self.count)


queue = queue.Queue(maxsize=10)

t1 = Bulka(queue)
t2 = Kotleta(queue, 20)

t1.start()
t2.start()

t1.join()
t2.join()
