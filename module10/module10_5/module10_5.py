import multiprocessing as mp

import threading

import time

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while True:
            line = file.readline().strip()
            if not line:
                break
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]



for filename in filenames:
    start_time = time.time()
    read_info(filename)
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения для файла {filename}: {execution_time} секунд")


if __name__ == '__main__':

    with mp.Pool() as pool:
        start_time = time.time()
        pool.map(read_info, filenames)
        end_time = time.time()
    execution_time = end_time - start_time
    print(f"Время выполнения многопроцессного подхода: {execution_time} секунд")