"""
Найдите количество положительных элементов в данном списке
"""

def number_positive_elements(a):
    count = 0
    for i in range(len(a)):
        if a[i] > 0:
            count += 1
    print(count)


def main():
    array = [int(word) for word in input().split()]
    number_positive_elements(array)


main()
