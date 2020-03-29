"""
Выведите значение наименьшего нечетного элемента списка,
а если в списке нет нечетных элементов - выведите число 0. 
"""

def min_odd_element(array):

    min_odd = 0

    for n in array:
        if n % 2 != 0 and min_odd % 2 == 0:
            min_odd = n
        elif n % 2 != 0 and n < min_odd:
            min_odd = n

    return min_odd


def main():
    a = [int(word) for word in input().split()]
    print(min_odd_element(a))


main()
