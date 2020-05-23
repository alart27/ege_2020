def ex_25():
    a = []
    n = 40
    count = 0
    for i in range(n):
        a.append(int(input))
    for i in range(n - 1):
        if a[i] % 100 == 10 or a[i + 1] % 100 == 10:
            count += 1
    print(count)

def bruteforce():
    a1 = [int(a) for a in input().split()]
    a2 = [int(a) for a in input().split()]
    a3 = [int(a) for a in input().split()]
    a4 = [int(a) for a in input().split()]
    a5 = [int(a) for a in input().split()]
    a6 = [int(a) for a in input().split()]

    max_sum = 0
    
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for e in range(2):
                    for x in range(2):
                        for y in range(2):
                            r = a1[i] + a2[j] + a3[k] + a4[e] + a5[x] + a6[y]
                            if r > max_sum and r % 5 != 0:
                                max_sum = r

    print(max_sum)

def optimal():

    max_sum = 0

    n = int(input())

    max_sum_5 = 0
    max_sum_4 = 0
    max_sum_3 = 0
    max_sum_2 = 0
    max_sum_1 = 0
    # d - delta
    d_5 = 0
    d_4 = 0
    d_3 = 0
    d_2 = 0
    d_1 = 0
    
    for i in range(n):
        pair = [int(a) for a in input().split()]
        for i in range(2):
            if pair[i] % 5 == 0:
                
                if pair[i] > d_4:
                    max_sum_4 -= d_4
                    d_4 = pair[i]
                    max_sum_4 += d_4
                    
                if pair[i] > d_3:
                    max_sum_3 -= d_3
                    d_3 = pair[i]
                    max_sum_3 += d_3
                    
                if pair[i] > d_2:
                    max_sum_2 -= d_2
                    d_2 = pair[i]
                    max_sum_2 += d_2
                    
                if pair[i] > d_1:
                    max_sum_1 -= d_1
                    d_1 = pair[i]
                    max_sum_1 += d_1

            if pair[i] % 5 == 4:
                
                if pair[i] > d_4:
                    max_sum_4 -= d_4
                    d_4 = pair[i]
                    max_sum_4 += d_4
                    
                if pair[i] > d_3:
                    max_sum_3 -= d_3
                    d_3 = pair[i]
                    max_sum_3 += d_3
                    
                if pair[i] > d_2:
                    max_sum_2 -= d_2
                    d_2 = pair[i]
                    max_sum_2 += d_2
                    
                if pair[i] > d_5:
                    max_sum_5 -= d_5
                    d_5 = pair[i]
                    max_sum_5 += d_5

            if pair[i] % 5 == 3:
                
                if pair[i] > d_4:
                    max_sum_4 -= d_4
                    d_4 = pair[i]
                    max_sum_4 += d_4
                    
                if pair[i] > d_3:
                    max_sum_3 -= d_3
                    d_3 = pair[i]
                    max_sum_3 += d_3
                    
                if pair[i] > d_5:
                    max_sum_5 -= d_5
                    d_5 = pair[i]
                    max_sum_5 += d_5
                    
                if pair[i] > d_1:
                    max_sum_1 -= d_1
                    d_1 = pair[i]
                    max_sum_1 += d_1

            if pair[i] % 5 == 2:
                
                if pair[i] > d_4:
                    max_sum_4 -= d_4
                    d_4 = pair[i]
                    max_sum_4 += d_4
                    
                if pair[i] > d_5:
                    max_sum_5 -= d_5
                    d_5 = pair[i]
                    max_sum_5 += d_5
                    
                if pair[i] > d_2:
                    max_sum_2 -= d_2
                    d_2 = pair[i]
                    max_sum_2 += d_2
                    
                if pair[i] > d_1:
                    max_sum_1 -= d_1
                    d_1 = pair[i]
                    max_sum_1 += d_1

            if pair[i] % 5 == 1:
                
                if pair[i] > d_5:
                    max_sum_5 -= d_5
                    d_5 = pair[i]
                    max_sum_5 += d_5
                    
                if pair[i] > d_3:
                    max_sum_3 -= d_3
                    d_3 = pair[i]
                    max_sum_3 += d_3
                    
                if pair[i] > d_2:
                    max_sum_2 -= d_2
                    d_2 = pair[i]
                    max_sum_2 += d_2
                    
                if pair[i] > d_1:
                    max_sum_1 -= d_1
                    d_1 = pair[i]
                    max_sum_1 += d_1
        d_5 = 0
        d_4 = 0
        d_3 = 0
        d_2 = 0
        d_1 = 0

    max_sum = max(max_sum_1, max_sum_2, max_sum_3, max_sum_4)
    print(max_sum)

def ex_27(choose_solution):
    if choose_solution == 2:
        bruteforce()
    if choose_solution == 4:
        optimal()

def main():
    print('2 - BRUTEFORCE, 4 - OPTIMAL')
    ex_27(int(input()))
    #ex_25



main()


          
