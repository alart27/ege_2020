"""
Выведите значение наименьшего из всех положительных элементов в списке.
Известно, что в списке есть хотя бы один положительный элемент,
а значения всех элементов списка по модулю не превосходят 1000. 
"""

def min_positive_element(array):

    min_pos = 1001
    
    for number in array:
        if number < min_pos and number > 0:
            min_pos = number

    return min_pos


def main():
    a = [int(word) for word in input().split()]
    print(min_positive_element(a))


main()
