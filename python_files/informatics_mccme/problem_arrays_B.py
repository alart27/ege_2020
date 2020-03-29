"""
informatis 3153
Выведите все четные элементы списка
"""

def even_elements(a):
    for i in range(len(a)):
        if a[i] % 2 == 0:
            print(a[i], end = ' ')


def main():
    array = [int(word) for word in input().split()]
    even_elements(array)


main()
