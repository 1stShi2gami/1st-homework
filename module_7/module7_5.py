import os  # для работы с файлами и директориями
import time  # для форматирования времени

directory = "."  # задаем текущую папку(Этот код можно использовать для анализа файлов в любой папке. Просто измените переменную directory на нужный путь.)

# Используем os.walk для обхода всех подкаталогов и файлов
for root, dirs, files in os.walk(directory):
    for file in files:
        # Формируем полный путь к файлу
        filepath = os.path.join(root, file)

        # Получаем время последнего изменения файла
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

        # Получаем размер файла в байтах
        filesize = os.path.getsize(filepath)

        # Получаем родительскую директорию файла
        parent_dir = os.path.dirname(filepath)

        # Выводим информацию о файле
        print(f'Файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
