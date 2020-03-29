"""
Non-recursive Euclid
"""


def exchange(a, b):
    if b > a:
        t = b
        b = a
        a = t
    return a, b

def nod(a, b):
    while b > 0:
        #a, b = exchange(a, b)
        k = b
        b = a % b
        a = k
    return a


def main():
    a = int(input())
    b = int(input())
    print(nod(a, b))


main()
