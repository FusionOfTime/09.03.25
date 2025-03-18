"""
Этот модуль содержит функции для определения
является ли сумма квадратов всех его элементов пятизначным числом.
"""

import math
def five_digit_number(digit):
    """
    Определяет, является ли заданное число пятизначным.

    Args:
        digit: Целое число.

    Returns:
        None.  Выводит "YES" если число пятизначное, "NO" в противном случае.
    """
    if 10000 <= digit <= 99999:
        print("YES")
    else:
        print("NO")

def main():
    """
    Основная функция программы.

    Считывает массив целых чисел из ввода, вычисляет сумму квадратов его элементов,
    и определяет, является ли эта сумма пятизначным числом, вызывая функцию `five_digit_number`.
    """
    n = int(input())
    array_str = input().split()
    array = []
    for s in array_str:
        array.append(int(s))

    sum_of_squares = 0
    for x in array:
        sum_of_squares += math.pow(x, 2)
    five_digit_number(sum_of_squares)



if __name__ == '__main__':
    main()