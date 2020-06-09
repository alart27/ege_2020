def bruteforce():
    a = []
    max_sum = 0
    for i in range(5):
        part = [int(a) for a in input().split()]
        a.append(part)

    for i in range(3):
        for j in range(3):
            for k in range(3):
                for e in range(3):
                    for z in range(3):
                        summ = a[0][i] + a[1][j] + a[2][k] + a[3][e] + a[4][z]
                        if summ % 3 != 0 and summ > max_sum:
                            max_sum = summ
    print(max_sum)

def optimal():
    max_sum = 0
    n = int(input())
    min_delta = -1
    delta = 0
    
    for i in range(n):
        part = [int(a) for a in input().split()]
        a = part[0]
        b = part[1]
        c = part[2]
        if a > b:
            t = a
            a = b
            b = t
        if a > c:
            t = a
            a = c
            c = t
        if b > c:
            t = b
            b = c
            c = t
        # sorted a<b<c
        if c-a % 3 != 0:
            delta = c-a
        elif c-b % 3 != 0:
            delta = c-b
            
        max_sum += max(a, b, c)
        if min_delta < 0 or min_delta > delta :
            min_delta = delta
            

    if max_sum % 3 == 0:
        if min_delta == 0:
            print(0)
        else:
            print(max_sum - min_delta)
    else:
        print(max_sum)
            
        

def main():
    #bruteforce()
    optimal()

main()
    
