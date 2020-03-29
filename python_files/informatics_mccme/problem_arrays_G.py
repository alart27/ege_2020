"""
Дан список чисел.
Выведите значение наибольшего элемента в списке,
а затем индекс этого элемента в списке.
Если наибольших элементов несколько, выведите индекс первого из них.
"""

def max_element(array):
    
    max_el = array[0]
    k = 0
    
    for i in range(1, len(array)):
        if array[i] > max_el:
            max_el = array[i]
            k = i

    print(max_el, k)


def main():
    a = [int(word) for word in input().split()]
    max_element(a)


main()
