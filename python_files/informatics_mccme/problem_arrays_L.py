"""
Выведите элементы данного списка в обратном порядке, не изменяя сам список.
Вводится список чисел. Все числа списка находятся на одной строке.
"""

def solution(array):
    for i in range(len(array)):
        print(array[len(array) - 1 - i], end = ' ')


def main():
    a = [int(word) for word in input().split()]
    solution(a)


main()
