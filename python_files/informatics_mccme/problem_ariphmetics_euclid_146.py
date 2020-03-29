"""
Даны две рациональные дроби: a/b и c/d.
Сложите их и результат представьте в виде несократимой дроби m/n.
"""

#a, b, c, d = [int(word) for word in input().split()]


def naive(a, b, c, d):
    m = a * d + b * c
    n = b * d
    i = 2

    while i <= n and i <= m:
        if n % i == 0 and m % i == 0:
            n = n // i
            m = m // i
        else:
            i = i + 1

    return m, n


def nod(a, b):
    """ simple euclid recursive

        nod(a, b) = nod(a-b, b)
        nod(0, a) = a
    """
    if b == 0:
        return a
    else:
        if a < b:
            return nod(b, a)
        else:
            return nod(a - b, b)


def solution(a, b, c, d):
    m = a * d + b * c
    n = b * d
    nod_mn = nod(m,n)

    return m // nod_mn, n // nod_mn

def main():
    a, b, c, d = [int(word) for word in input().split()]

##    print(nod(12, 15))
##    print(nod(7,4))
##    print(nod(6, 12))
##    print(nod(32, 48))

    m, n = solution(a,b,c,d)
    #m1, n1 = naive(a,b,c,d)

    #print(m,'/',n)
    print(m, n)
    #print(m1, n1)

main()


