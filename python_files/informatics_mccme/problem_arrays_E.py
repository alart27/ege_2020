"""
Дан список чисел.
Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет - не выводите ничего.
Если таких пар соседей несколько - выведите первую пару. 
"""

def first_pair(array):

##    flag = True
##    i = 1
##
##    while flag:
##        if i < len(array)-1:
##            if and (array[i] > 0 and array[i+1] > 0 or array[i] < 0 and array[i+1] < 0 or array[i] == 0 and array[i+1] == 0):
##            print(array[i], array[i+1])
##            flag = False
##        i += 1 

    for i in range(len(array)-1):
        if array[i] > 0 and array[i+1] > 0 or \
           array[i] < 0 and array[i+1] < 0 or \
           array[i] == 0 and array[i+1] == 0:
            return array[i], array[i+1]
            # break - не нужен

    return None, None


def main():
    array = [int(word) for word in input().split()]
    a, b = first_pair(array)
    if a is not None:
        print(a,b)


main()
