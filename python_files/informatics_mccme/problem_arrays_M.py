"""
Переставьте элементы данного списка в обратном порядке,
затем выведите элементы полученного списка. 
Эта задача отличается от предыдущей тем, что вам нужно изменить значения
элементов самого списка,
поменяв местами A[0] c A[n-1], A[1] с A[n-2],
а затем вывести элементы списка подряд. 
"""


def solution(array):
    for i in range(len(array) // 2):
        t = array[i]
        array[i] = array[len(array) - 1 - i]
        array[len(array) - 1 - i] = t

    return array


def main():
    a = [int(word) for word in input().split()]
    solution(a)
    for i in range(len(a)):
        print(a[i], end = ' ')


main()
