from Lab.mathematical_operations import *


def read_input():
    num1, sign, num2 = input().split(" ")
    num1 = float(num1)
    num2 = float(num2)
    return num1, sign, num2


number1, math_sign, number2 = read_input()


def calculate(num1, sign, num2):
    if sign == "/":
        result = divide(num1, num2)
        return result
    elif sign == "*":
        result = multiply(num1, num2)
        return result
    elif sign == "-":
        result = subtract(num1, num2)
        return result
    elif sign == "+":
        result = add(num1, num2)
        return result
    elif sign == "^":
        result = power(num1, num2)
        return result
    else:
        return f"Invalid sign {sign}"


def print_result(res):
    print(f"{res:.2f}")


print_result(calculate(number1, math_sign, number2))
