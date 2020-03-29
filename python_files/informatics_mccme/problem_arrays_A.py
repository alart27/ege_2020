"""
Выведите все элементы списка с четными индексами
"""

def even_elements(a):
    for i in range(0, len(a), 2):
        print(a[i], end = ' ')


def main():
    array = [int(word) for word in input().split()]
    even_elements(array)


main()
