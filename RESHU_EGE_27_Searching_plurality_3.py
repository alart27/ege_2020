"""
На плоскости задано множество точек с целочисленными координатами,
никакие две из которых не совпадают и никакие три не лежат на одной прямой.
Необходимо найти количество треугольников, обладающих следующими свойствами:

1) все вершины треугольника принадлежат заданному множеству;
2) ни одна вершина не лежит на осях координат;
3) треугольник не пересекается с осью Ox, но пересекается с осью Oy.

Входные данные
В первой строке задаётся N – количество точек в заданном множестве.
Каждая из следующих строк содержит два целых числа x и y – координаты очередной
точки. Гарантируется, что 1 ≤ N ≤ 10000, –1000 ≤ x, y ≤ 1000,
никакие две точки не совпадают, никакие три не лежат на одной прямой.

Выходные данные
Необходимо вывести единственное число:
количество удовлетворяющих требованиям треугольников.

Here is a problem with negative numbers
"""

def bruteforce():
    return 0



def optimal():
    n = int(input())
    quaters = [0, 0, 0, 0]
    answer = 0
    
    for i in range(n):
        t = [int(a) for a in input().split()]
        if t[0] > 0 and t[1] > 0:
            quaters[0] += 1
        elif t[0] < 0 and t[1] > 0:
            quaters[1] += 1
        elif t[0] < 0 and t[1] < 0:
            quaters[2] += 1
        elif t[0] > 0 and t[1] < 0:
            quaters[3] += 1

    for i in range(n):
        if quaters[i] >= 3:
            answer += quaters[i] * (quaters[i] - 1) * (quaters[i] - 2) / 6

    print(answer)


def main():
    bruteforce()
    optimal()

main()


