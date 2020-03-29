"""
Дан список. Выведите те его элементы, которые встречаются в списке
только один раз.
Элементы нужно выводить в том порядке, в котором они встречаются в списке.
"""


def solution(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if i != j and array[i] == array[j]:
                break
        else:
            print(array[i], end=' ')


def main():
    a = [int(word) for word in input().split()]
    solution(a)


main()
