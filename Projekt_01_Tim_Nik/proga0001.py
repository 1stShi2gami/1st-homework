import tkinter as tk
from tkinter import *
import sys


def imt():
    new_window_1 = Toplevel(window)
    new_window_1('Калькулятор 1')  # заголовок окна
    new_window_1('300x500')  # размер окна
    # запрос информации от пользователей
    the_height = float(input("Введите рост см: "))
    the_weight = float(input("введите вес кг: "))
    number1_entry = tk.Entry(window, width=28)  # Текстовое поле для введения Пользователя
    number1_entry.place(x=100, y=75)
    number2_entry = tk.Entry(window, width=28)  # Текстовое поле для введения Пользователя
    number2_entry.place(x=100, y=150)
    answer_entry = tk.Entry(window, width=28)  # Текстовое поле вывода(то есть итог после сложения)
    answer_entry.place(x=100, y=300)
    number1 = tk.Label(window, text='Введите первое число:')  # Виджет для надписи IV
    number1.place(x=100, y=50)
    number2 = tk.Label(window, text='Введите второе число:')  # IV
    number2.place(x=100, y=125)
    answer = tk.Label(window, text='Ответ:')  # IV
    answer.place(x=100, y=275)
    # определение функции для ИМТ
    the_BMI = the_weight / (the_height / 100) ** 2
    # распечатка ИМТ
    print("Ваш индекс массы тела", the_BMI)
    # используя условия if-elif-else
    if the_BMI <= 18.5:
        print("Упс! У вас недостаточный вес.")
    elif the_BMI <= 24.9:
        print("Потрясающий! Вы здоровы.")
    elif the_BMI <= 29.9:
        print("Эээ! У вас избыточный вес.")
    else:
        print("Сиш! Вы страдаете ожирением.")


# создание окна
window = tk.Tk()  # создание окна
window.title('Калькулятор')  # заголовок окна
window.geometry('300x500')  # размер окна


# кнопки для функций
knopka_imt = tk.Button(window, text='ИМТ', width=42, height=3, bg='cornsilk1', fg='black',
                       font=('Constantia', 9, 'bold'), command=imt)
knopka_imt.place(x=0, y=100)
knopka_imt.grid(column=1,row=1,sticky=NSEW)
window.grid_columnconfigure(1,weight=1)
knopka_sip = tk.Button(window, text='Скорость инфузии \n препарата', width=42, height=3, bg='cornsilk1', fg='black',
                       font=('Constantia', 9, 'bold'))  # ,command='добавить исполнительную функицю')
knopka_sip.place(x=0, y=160)
knopka_sip.grid(column=1,row=2,sticky=NSEW)
window.grid_columnconfigure(1,weight=1)
knopka_dk = tk.Button(window, text='Дефицит калия', width=42, height=3, bg='cornsilk1', fg='black',
                      font=('Constantia', 9, 'bold'))  # ,command='добавить исполнительную функицю')
knopka_dk.place(x=0, y=220)
knopka_dk.grid(column=1,row=3,sticky=NSEW)
window.grid_columnconfigure(1,weight=1)
knopka_svvp = tk.Button(window, text='Скорость внутривенного \n капельного \n введения препарата', width=42, height=3,
                        bg='cornsilk1', fg='black',
                        font=('Constantia', 9, 'bold'))  # ,command='добавить исполнительную функицю')
knopka_svvp.place(x=0, y=280)
knopka_svvp.grid(column=1,row=4,sticky=NSEW)
window.grid_columnconfigure(1,weight=1)

window.mainloop()  # запуск окна
