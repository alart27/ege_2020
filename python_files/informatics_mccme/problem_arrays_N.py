"""
Переставьте соседние элементы списка (A[0] c A[1], A[2] c A[3] и т.д.).
Если элементов нечетное число, то последний элемент остается на своем месте.
"""


def solution(array):
    for i in range(0, len(array) - 1 - len(array) % 2, 2):
        t = array[i]
        array[i] = array[i+1]
        array[i+1] = t
    return array


def main():
    a = [int(word) for word in input().split()]
    solution(a)
    for i in range(len(a)):
        print(a[i], end = ' ')


main()
