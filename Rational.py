# Вычисления с рациональными числами

import math


def mathout(op, x, y):  # функция вывода
    print(op(x, y))


def sum(a, b):  # функция сложения
    return a + b


def sub(a, b):  # функция вычетания
    return a - b


def mult(a, b):  # функция умножения
    return a * b


def div(a, b):  # функция деления
    return a / b


def degree(a, b):  # функция возведения в степень
    return a**b


def logarifm(a, b):  # функция логарифмирования
    return math.log(a, b)


a = input("Ведите первую цифру:\n")  # Ввод переменной а
operator = input("Оператор (+, -, *, /, ^, log):\n")
b = input("Ведите вторую цифру:\n")  # Ввод переменной b

a = float(a)
b = float(b)

out = None

if operator == "+":
    mathout(sum, a, b)
elif operator == "-":
    mathout(sub, a, b)
elif operator == "*":
    mathout(mult, a, b)
elif operator == "/":
    mathout(div, a, b)
elif operator == "log":
    mathout(logarifm, a, b)
elif operator == "^":
    mathout(degree, a, b)
