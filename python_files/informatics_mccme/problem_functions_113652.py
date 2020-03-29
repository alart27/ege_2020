"""
informatics 113652

Определить можно ли с использованием только операций «прибавить 3» и
«прибавить 5» получить из числа 1 число N (N - натуральное,
не превышает 10^6).
"""


def naive(n):
    while n > 0:
        if n == 1:
            print('YES')
            break
        if n > 5:
            n = n - 5
        else: n -= 3
        if n % 3 == 0 and n >= 0:
            print('YES')
            break
        if n < 0:
            print('NO')


def bruteforce(n):
    """ n-1 = 5*m + 3*k
        m <= (n-1)/5
        k <= (n-1)/3

        try this for all possible (m, k) pairs
    """
    for m in range((n-1)//5 + 1):
        for k in range((n-1)//3 + 1):
            if n-1 == 5*m + 3*k:
                return True

    return False


def math_hack(n):
    return n not in [0,2,3,5,8]


def recursive(n):
    print("recursive:", n)
    if n == 1:
        return True
    elif n < 1:
        return False
    else:
        return recursive(n-3) or recursive(n-5)
    

def print_all_good_numbers_table():
    size = 4
    for k in range(size):
        for m in range(size):
            print(5 * m + k * 3 + 1, end=' ')
        print()
            

def main():
    n = int(input())

    #answer = math_hack(n)
    answer = recursive(n)
    if answer:
        print("YES")
    else:
        print("NO")

    #print_all_good_numbers_table()

main()

    
