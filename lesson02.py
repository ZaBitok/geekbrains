# Практическое задание

"""
1) Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого
элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя,
а указать явно, в программе.
"""

# my_list = ['Ivan', 35, 'ZaBitok', 'Eva', 9.99, 'GitHub', True]
# for i in my_list:
#     print(type(i))

"""
2)Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с
индексами 0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Для заполнения
списка элементов необходимо использовать функцию input().
"""

# information_request = input('Добавит элемент в список? y/n: ')
# user_list = []
# my_list = []
# while information_request == 'y':
#     user_list.append(input('Какой элемент добавить: '))
#     information_request = input('Добавит еще элемент в список? y/n: ')
#
# if len(user_list) != 0:
#     for i in range(0, len(user_list), 2):
#         my_list.append(user_list[i])
#     for i in range(1, len(user_list), 2):
#         my_list.insert((i - 1), user_list[i])
#         print(user_list)
#         print(my_list)

"""
3) Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится
месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
"""

# Решение через list

# winter = [12, 1, 2]
# spring = [3, 4, 5]
# summer = [6, 7, 8]
# fall = [9, 10, 11]
# month = int(input('Введите месяц числом: '))
# if month in winter:
#     print('Зима')
# elif month in spring:
#     print('Весна')
# elif month in summer:
#     print('Лето')
# elif month in fall:
#     print('Осень')
# else:
#     print('Что-то пошло не по плану')

# Решение через dict

# my_dict = {
#     1: 'Зима',
#     2: 'Зима',
#     3: 'Весна',
#     4: 'Весна',
#     5: 'Весна',
#     6: 'Лето',
#     7: 'Лето',
#     8: 'Лето',
#     9: 'Осень',
#     10: 'Осень',
#     11: 'Осень',
#     12: 'Зима'}
# month = int(input('Введите месяц числом: '))
# print(my_dict.get(month))

"""
4) Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.
"""

# user_line = input('Введите строку из нескольких слов: ').split()
# i = 1
# for my_word in user_line:
#     print(f'{i}) {my_word[0:10]}')
#     i += 1

"""
5) Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].
"""

# my_list = [7, 5, 3, 3, 2]
# user_rating = int(input('Введите рейтинг: '))
# my_list.append(user_rating)
# my_list.sort()
# my_list.reverse()
# print(my_list)

"""
6) *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит 
информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
(характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать
программно, т.е. запрашивать все данные у пользователя.
Пример готовой структуры:
[
    (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
    (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
    (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
]
Необходимо собрать аналитику о товарах. Реализовать словарь, в котором каждый ключ — характеристика товара, например
название, а значение — список значений-характеристик, например список названий товаров.
Пример:
{
    “название”: [“компьютер”, “принтер”, “сканер”],
    “цена”: [20000, 6000, 2000],
    “количество”: [5, 2, 7],
    “ед”: [“шт.”]
}
"""
