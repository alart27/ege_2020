"""
Дан список чисел.
Выведите все элементы списка, которые больше предыдущего элемента.
"""

def elements_that_stronger_previous(array):
    for i in range(1, len(array)):
        if array[i-1] < array[i]:
            print(array[i], end = ' ')


def main():
    a = [int(word) for word in input().split()]
    elements_that_stronger_previous(a)


main()
