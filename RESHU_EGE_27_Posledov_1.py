"""
По каналу связи передается последовательность положительных целых чисел,
все числа не превышают 1000, их количество заранее неизвестно.
Каждое число передается в виде отдельной текстовой строки,
содержащей десятичную запись числа. Признаком конца передаваемой
последовательности является число 0. Участок последовательности
от элемента  до элемента
называется подъемом, если на этом участке каждое следующее число больше
предыдущего. Высотой подъема называется разность.
Напишите эффективную программу, которая вычисляет наибольшую высоту среди всех
подъемов последовательности. Если в последовательности нет ни одного подъема,
программа выдает 0. Программа должна напечатать отчет по следующей форме:
Получено ... чисел Наибольшая высота подъема: …

description(bruteforce):
С помощью 2 вложенных циклов перебираем
все высоты подьема, находим из них наибольшую

description(optimal):
Every new number is read and obrabat in cycle while,
so iteration number is number of got numbers
Чтобы посчитать, сколько чисел было получено, используем счетчик,
подсчитывающий число интераций
if posledov is rising we increase delta, else we sravnivaem maximum delta and
the current one and obnulyaem her

(sorry for that description, print on russian is pain on this keyboard)
""" 
def bruteforce():
    a = []
    b = -1
    delta = 0
    while b != 0:
        b = int(input())
        if b != 0:
            a.append(b)

    for i in range(len(a)):
        for j in range(i+1, len(a)):
            if a[j] > a[i] and delta < a[j] - a[i]:
                delta = a[j] - a[i]
    print('Получено: ', len(a), ' чисел')
    print('Наибольшая высота подъема: ', delta)

def optimal():
    b = -1
    delta = 0
    d_max = 0
    count = 0
    while b != 0:
        a = b
        b = int(input())
        if b == 0:
            break
        if b > a and a != -1:
            delta += b - a
        else:
            if d_max < delta:
                d_max = delta
            delta = 0

        count += 1
    print('Получено: ', count, ' чисел')
    print('Наибольшая высота подъема: ', d_max)

def main():
    #bruteforce()
    optimal()


main()
