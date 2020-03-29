"""
В списке все элементы различны.
Поменяйте местами минимальный и максимальный элемент этого списка. 
"""

def solution(array):
    
    min_num = array[0]
    max_num = array[0]
    index_min = 0
    index_max = 0
    
    for i in range(len(array)):
        if min_num > array[i]:
            min_num = array[i]
            index_min = i
        if max_num < array[i]:
            max_num = array[i]
            index_max = i

    array[index_max] = min_num
    array[index_min] = max_num

    return array


def main():
    a = [int(word) for word in input().split()]
    solution(a)
    for n in a:
        print(n, end = ' ')


main()
