"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""


def my_func(x, y, z):
    return (x + y + z) - min(x, y, z)


print(my_func(2, 5, 7))
