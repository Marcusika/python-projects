import math
from math import*
ecuation_signs = ["+", "-", "x", "/", "**", "sqrt"]
sign = input("Choose an ecuation sign (+, -, x, /, **, sqrt): ")
while sign not in ecuation_signs:
    sign = input("Choose an ecuation sign (+, -, x, /, **, sqrt): ")

if sign == "+":
    add_1 = input("Choose your first number: ")
    while not add_1.isnumeric():
        add_1 = input("Choose your first number: ")
    add_2 = input("Choose your second number: ")
    while not add_2.isnumeric():
        add_2 = input("Choose your second number: ")
    print(float(add_1) + float(add_2))
elif sign == "-":
    sub_1 = input("Choose your first number: ")
    while not sub_1.isnumeric():
        sub_1 = input("Choose your first number: ")
    sub_2 = input("Choose your second number: ")
    while not sub_2.isnumeric():
        sub_2 = input("Choose your second number: ")
    print(float(sub_1) - float(sub_2))
elif sign == "/":
    div_1 = input("Choose your first number: ")
    while not div_1.isnumeric():
        div_1 = input("Choose your first number: ")
    div_2 = input("Choose your second number: ")
    while not div_2.isnumeric():
        div_2 = input("Choose your second number: ")
    print(float(div_1) / float(div_2))
elif sign == "*":
    mlt_1 = input("Choose your first number: ")
    while not mlt_1.isnumeric():
        mlt_1 = input("Choose your first number: ")
    mlt_2 = input("Choose your second number: ")
    while not mlt_2.isnumeric():
        mlt_2 = input("Choose your second number: ")
    print(float(mlt_1) * float(mlt_2))
elif sign == "sqrt":
    sqrt_1 = input("Choose your number: ")
    while not sqrt_1.isnumeric():
        sqrt_1 = input("Choose your number: ")
    print(sqrt(float(sqrt_1)))
elif sign == "**":
    exp_1 = input("Choose your first number: ")
    while not exp_1.isnumeric():
        exp_1 = input("Choose your first number: ")
    exp_2 = input("Choose your second number: ")
    while not exp_2.isnumeric():
        exp_2 = input("Choose your second number: ")
    print(float(exp_1) ** float(exp_2))

    