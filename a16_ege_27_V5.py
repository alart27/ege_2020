"""
Variant 5 27 EGE (where is the mistake?)
"""

def optimal():
    n = int(input())
    trash = [-1 for i in range(5)]
    n_113 = 0
    n_not_113 = 0
    pairs = 0
    
    for i in range(n):
        num = int(input())
        if num % 113 != 0:
            pairs += n_113
        else:
            pairs += n_113 + n_not_113

        if trash[0] % 113 == 0:
            n_113 += 1
        else:
            n_not_113 += 1

        for j in range(4):
            trash[j] = trash[j+1]
        trash[4] = num

    print(pairs)

def main():
    optimal()


main()
