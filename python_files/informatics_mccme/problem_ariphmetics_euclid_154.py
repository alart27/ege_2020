"""
Даны два натуральных числа A и B. Требуется найти их наибольший общий делитель.
"""

def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)

def smart_recursive():
    a, b = [int(word) for word in input().split()]
    print(nod(a, b))

smart_recursive()
