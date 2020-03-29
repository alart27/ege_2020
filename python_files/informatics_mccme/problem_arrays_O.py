"""
Циклически сдвиньте элементы списка вправо (A[0] переходит на место A[1], A[1]
на место A[2], ..., последний элемент переходит на место A[0]). 
Используйте минимально возможное количество операций присваивания. 
"""


def solution_1(a):
    """ попарные обмены
        0 <> 1; 0 <> 2 и тд
    """
    for i in range(1, len(a)):
        t = a[0]
        a[0] = a[i]
        a[i] = t
    return a


def solution_2(a):
    """ сохранили крайний правый, остальные сдвинули, начиная с предпоследнего """

    temp = a[len(a)-1]   # python: temp = a[-1]
    
    for i in range(len(a)-2, -1, -1):
        a[i+1] = a[i]

    a[0] = temp

    return a


    
def main():
    a = [int(word) for word in input().split()]
    result = solution_2(a)
    #for i in result:
    #    print(i, end = ' ')

    print(' '.join(str(elem) for elem in result))

main()
