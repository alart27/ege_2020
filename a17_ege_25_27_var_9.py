def ex_25():
    a = []
    n = 6
    for i in range(n):
        a.append(int(input()))

    count = 0
    for i in range(n):
        if a[i] > 1000 and a[i] % 100 == 10:
            count += 1

    for i in range(n):
        if a[i] > 1000 and a[i] % 100 == 10:
            a[i] = count

    print(a)

def bruteforce():
    n = int(input())
    a = []
    count = 0
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        for j in range(i + 1, n):
            product = a[i]*a[j]
            if product % 58 == 0:
                count += 1
    print(count)

def optimal():
    n = int(input())
    n_58 = 0
    n_29 = 0
    n_2 = 0
    not_all = 0

    for i in range(n):
        num = int(input())
        if num % 58 == 0:
            n_58 += 1
        elif num % 2 == 0:
            n_2 += 1
        elif num % 29 == 0:
            n_29 += 1
        else:
            not_all += 1

    count = n_29 * n_2 + n_58 * (n_29 + n_2 + not_all) + (n_58 * (n_58 - 1)) / 2

    print(int(count))


def main():
#    ex_25()
    optimal()
#    bruteforce()



main()
