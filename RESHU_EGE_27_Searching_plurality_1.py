"""
На ускорителе для большого числа частиц производятся замеры скорости
каждой из них. Скорость частицы — это целое число (положительное,
отрицательное или 0). Частиц, скорость которых измерена,
может быть очень много, но не может быть меньше трёх.
Скорости всех частиц различны. При обработке результатов в каждой серии
эксперимента отбирается основное множество скоростей.
Это такое непустое множество скоростей частиц (в него могут войти как скорость
одной частицы, так и скорости всех частиц серии), для которого произведение
скоростей является максимальным среди всех возможных множеств.
При нахождении произведения знак числа учитывается.
Если есть несколько таких множеств,
то основным считается то, которое содержит наибольшее количество элементов.

На вход программе в первой строке подаётся количество частиц N.
В каждой из последующих N строк записано одно целое число,
по абсолютной величине не превышающее 10^9.

Программа должна вывести в порядке возрастания номера частиц,
скорости которых принадлежат основному множеству данной серии.
Нумерация частиц ведётся с единицы.

discription(bruteforce):
I decided to wrtite discripts on paper
"""

def bruteforce():
    n = int(input())
    a = []
    neg_num = 0
    max_neg = -2000000000
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        if a[i] < 0:
            neg_num += 1
            if a[i] > max_neg:
                max_neg = a[i]
    if neg_num % 2 == 0:
        for i in range(n):
            if a[i] != 0:
                print(i+1, end = ' ')
    else:
        for i in range(n):
            if a[i] != 0 and a[i] != max_neg:
                print(i+1, end = ' ')

def optimal():
    n = int(input())
    flags = [1 for i in range(n)]
    neg_num = 0
    max_neg = -2000000000
    for i in range(n):
        num = int(input())
        if num < 0:
            neg_num += 1
            if num > max_neg:
                max_neg = num
                flags[i] = max_neg
        if num == 0:
            flags[i] = 0
    for i in range(n):
        if flags[i] != 0 or flags[i] != max_neg:
            print(i+1, end = ' ')
        
    
def main():
    #bruteforce()
    optimal()

main()


        



        