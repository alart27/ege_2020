"""
Дан список из чисел и индекс элемента в списке k.
Удалите из списка элемент с индексом k,
сдвинув влево все элементы, стоящие правее элемента с индексом k.
"""

def solution(array, index):
    for i in range(index + 1, len(array)):
        temp = array[i]
        array[i-1] = temp
    array.pop(-1)

    return array


def main():
    a = [int(word) for word in input().split()]
    k = int(input())
    ans = solution(a, k)
    for i in ans:
        print(i, end = ' ')


main()
