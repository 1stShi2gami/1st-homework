from threading import Thread
from time import sleep
import threading
from datetime import datetime


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for i in range(1, word_count + 1):
            word = f'Какое-то слово № {i}\n'
            file.write(word)
            sleep(0.1)
            print(f'Завершилась запись в {file_name}')

time_start = datetime.now()

print(write_words(10, 'example1.txt'))
print(write_words(30, 'example2.txt'))
print(write_words(200, 'example3.txt'))
print(write_words(100, 'example4.txt'))


time_stop = datetime.now()
time_res = time_stop - time_start


print(f'Время выполнения: {time_res}')

time2_start = datetime.now()

tr1 = Thread(target=write_words, args=(10, 'example5.txt'))
tr2 = Thread(target=write_words, args=(30, 'example6.txt'))
tr3 = Thread(target=write_words, args=(200, 'example7.txt'))
tr4 = Thread(target=write_words, args=(100, 'example8.txt'))

tr1.start()
tr2.start()
tr3.start()
tr4.start()

tr1.join()
tr2.join()
tr3.join()
tr4.join()

time2_stop = datetime.now()
time2_res = time2_stop - time2_start
print(f'Время работы потоков {time2_res}')
print(f'Использование Потоков быстрее функций на {time_res-time2_res} секунд')










# import threading
# import time
#
# def func1():
#     for i in range(10):
#         time.sleep(0.5)
#         print(i, threading.current_thread())
#
# def func2(x):
#     for i in range(10):
#         time.sleep(1)
#         print(i, threading.current_thread())
#
#
# thread = threading.Thread(target=func2, args=(1,), daemon=True)
# thread.start()
# print(thread.is_alive())
# func1()
# print(threading.enumerate())
# print(threading.current_thread())