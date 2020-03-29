"""
Дан список, упорядоченный по неубыванию элементов в нем.
Определите, сколько в нем различных элементов.
"""

def solution(array):

    count = 1
    n = array[0]

    for m in array:
        if n != m:
            count += 1
            n = m

    return count


def main():
    a = [int(word) for word in input().split()]
    print(solution(a))


main()
