"""
Этот модуль содержит функции для вычисления среднего арифметического
и нахождения чисел, превышающих это среднее.
"""
def arithmetic_mean(number_array: list[int]) -> int:
    """
       Вычисляет среднее арифметическое элементов массива.

       Args:
           number_array: Массив чисел (целых чисел).

       Returns:
           Среднее арифметическое чисел в массиве, или 0.0, если массив пуст.
       """
    if not number_array:
        return 0
    return sum(number_array) / len(number_array)
def main():
    """
       Считывает числа с ввода, пока не будет введен 0,
       создает массив и вычисляет его среднее арифметическое.
       """
    numbers_array = []
    number = int(input())
    while number != 0:
        numbers_array.append(number)
        number = int(input())
    average = arithmetic_mean(numbers_array)
    greater_than_average = []
    for num in numbers_array:
        if num > average:
            greater_than_average.append(num)
    print(len(greater_than_average))
    print(*greater_than_average)


if __name__ == '__main__':
    main()