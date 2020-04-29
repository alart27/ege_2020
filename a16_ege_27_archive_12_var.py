"""
Дана последовательность N целых положительных чисел.
Рассматриваются все пары элементов последовательности,
сумма которых делится на m = 80.
Среди всех таких пар нужно найти и вывести пару с максимальным
произведением элементов.
Если одинаковое максимальное произведение имеют несколько пар,
можно вывести любую из них.
Если подходящих пар в последовательности нет, нужно вывести два нуля.
"""
def bruteforce():
    n = int(input())
    m = 80
    max_product = 0
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        for j in range(i + 1, n):
            summ = a[i] + a[j]
            product = a[i] * a[j]
            if summ % m == 0 and product > max_product:
                max_product = product
                left = a[i]
                right = a[j]

    if left > right:
        t = left
        left = right
        right = t

    if max_product != 0:
        print(left, right)
    else:
        print('0 0')

def optimal():
    n = int(input())
    m = 80
    max_product = 0
    a = [-1 for i in range(m)]
    max_0 = 0
    
    for i in range(n):
        num = int(input())
        if num % m == 0 and num > max_0:
            if num < a[0]:
                max_0 = num
            else:
                max_0 = a[0]
                a[0] = num
            product = max_0 * a[0]
            if product > max_product:
                max_product = product
                left = max_0
                right = a[0]
                
        elif num > a[num % m]:
            a[num % m] = num
            product = a[num % m] * a[80 - num % m]
            if product > max_product:
                max_product = product
                left = a[num % m]
                right = a[80 - num % m]

    if left > right:
        t = left
        left = right
        right = t
        
    if max_product != 0:
        print(left, right)
    else:
        print('0 0')
            
def main():
#    bruteforce()
    optimal()

main()



