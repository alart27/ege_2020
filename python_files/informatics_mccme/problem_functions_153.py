"""
Требуется найти N-е число Фибоначчи.
Примечание. В программе запрещается использовать циклы.
"""

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)

def main():
    n = int(input())
    b = fib(n)
    print(b)

main()
