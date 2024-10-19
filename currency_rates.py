from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests


def update_t_label(event):
    code = t_combobox.get()
    if code:
        name = course.get(code, 'Валюта не найдена')
        t_label.config(text=name)
    else:
        t_label.config(text='Выберите валюту')


def update_b_label_1(event):
    code = b_combobox_1.get()
    if code:
        name = course.get(code, 'Валюта не найдена')
        b_label_1.config(text=name)
    else:
        b_label_1.config(text='Выберите валюту')


def update_b_label_2(event):
    code = b_combobox_2.get()
    if code:
        name = course.get(code, 'Валюта не найдена')
        b_label_2.config(text=name)
    else:
        b_label_2.config(text='Выберите валюту')


def exchange():
    t_code = t_combobox.get()
    b_code_1 = b_combobox_1.get()
    b_code_2 = b_combobox_2.get()

    if t_code and b_code_1 and b_code_2:
        try:
            # Получаем курс для первой базовой валюты
            response_1 = requests.get(f'https://open.er-api.com/v6/latest/{b_code_1}')
            response_1.raise_for_status()
            data_1 = response_1.json()

            # Получаем курс для второй базовой валюты
            response_2 = requests.get(f'https://open.er-api.com/v6/latest/{b_code_2}')
            response_2.raise_for_status()
            data_2 = response_2.json()

            if t_code in data_1['rates'] and t_code in data_2['rates']:
                exchange_rate_1 = data_1['rates'][t_code]
                exchange_rate_2 = data_2['rates'][t_code]
                t_name = course[t_code]
                b_name_1 = course[b_code_1]
                b_name_2 = course[b_code_2]
                mb.showinfo('Курсы обмена', f'Курс {exchange_rate_1:.2f} {t_name} за 1 {b_name_1}\n'
                                            f'Курс {exchange_rate_2:.2f} {t_name} за 1 {b_name_2}')
            else:
                mb.showerror('Ошибка', 'Выбранная целевая валюта не найдена для одной из базовых валют')
        except Exception as e:
            mb.showerror('Ошибка', f'Произошла ошибка: {e}!')
    else:
        mb.showwarning('Внимание', 'Введите коды всех валют!')


course = {
    'RUB': 'Российский рубль',
    'EUR': 'Евро',
    'GBP': 'Британский фунт стерлингов',
    'JPY': 'Японская иена',
    'CNY': 'Китайский юань',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум',
    'CHF': 'Швейцарский франк',
    'AED': 'Дирхам ОАЭ',
    'CAD': 'Канадский доллар',
    'USD': 'Доллар США',
    'AUD': 'Австралийский доллар',
    'SEK': 'Шведская крона',
    'NOK': 'Норвежская крона',
    'PLN': 'Польский злотый',
    'TRY': 'Турецкая лира',
    'MXN': 'Мексиканское песо',
    'BRL': 'Бразильский реал',
    'INR': 'Индийская рупия',
    'ZAR': 'Южноафриканский рэнд'
}

window = Tk()
window.title('Курсы валют')
window.geometry('400x360')

# Первая базовая валюта
Label(window, text='Первая базовая валюта: ', font=('Arial', 12, 'bold')).pack(padx=10, pady=10)
b_combobox_1 = ttk.Combobox(window, values=list(course.keys()), font=('Arial', 12))
b_combobox_1.pack(padx=10, pady=(0, 10))
b_combobox_1.bind('<<ComboboxSelected>>', update_b_label_1)
b_label_1 = ttk.Label(window, font=('Arial', 12))
b_label_1.pack(padx=10, pady=(0, 10))

# Вторая базовая валюта
Label(window, text='Вторая базовая валюта: ', font=('Arial', 12, 'bold')).pack(padx=10, pady=(0, 10))
b_combobox_2 = ttk.Combobox(window, values=list(course.keys()), font=('Arial', 12))
b_combobox_2.pack(padx=10, pady=(0, 10))
b_combobox_2.bind('<<ComboboxSelected>>', update_b_label_2)
b_label_2 = ttk.Label(window, font=('Arial', 12))
b_label_2.pack(padx=10, pady=(0, 10))

# Целевая валюта
Label(window, text='Целевая валюта: ', font=('Arial', 12, 'bold')).pack(padx=10, pady=(0, 10))
t_combobox = ttk.Combobox(window, values=list(course.keys()), font=('Arial', 12))
t_combobox.pack(padx=10, pady=(0, 10))
t_combobox.bind('<<ComboboxSelected>>', update_t_label)
t_label = ttk.Label(window, font=('Arial', 12))
t_label.pack(padx=10, pady=(0, 10))

ttk.Button(window, text='Получить курсы обмена', command=exchange, style='Custom.TButton').pack(padx=10, pady=(0, 10))
style = ttk.Style()
style.configure('Custom.TButton', font=('Arial', 12))

window.mainloop()
