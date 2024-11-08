import threading
import time
import random



class Bank(threading.Thread):
    def __init__(self, balance=0):
        super().__init__()
        self.lock = threading.Lock()
        self.balance = balance



    def deposit(self):
        for i in range(100): # 100 транзакций
            amount = random.randint(50,500) # случайное число
            self.lock.acquire() # открытие замка
            self.balance += amount # увеличение баланса
            if self.balance >= 500:
                print(f'Пополнение {amount}, баланс: {self.balance}')
                if self.lock.locked():
                    self.lock.release()
            else:
                self.lock.release()
            time.sleep(0.001)

    def take(self):
        for i in range(100):
            amount = random.randint(50,500)
            print(f'Запрос на {amount}')
            self.lock.acquire()
            if self.balance >= amount:
                self.balance -= amount # уменьшение баланса
                print(f'Снятие {amount}, баланс: {self.balance}')
                if self.lock.locked():
                    self.lock.release()
            else:
                self.lock.release()
            time.sleep(0.001)



bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')







