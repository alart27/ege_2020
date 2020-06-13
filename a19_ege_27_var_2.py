def bruteforce():
    n = int(input())
    a = []
    m = 1011
    max_sum = 0
    for i in range(n):
        a.append(int(input()))
    for i in range(n):
        for j in range(i+1, n):
            summ = a[i] + a[j]
            if a[i] > a[j] and summ % m == 0 and max_sum < summ:
                max_sum = summ
                l = a[i]
                r = a[j]
    print(l, r)

def optimal():
    n = int(input())
    m = 1011
    max_sum = 0
    rests = [0 for i in range(m)]
    for i in range(n):
        num = int(input())
        index = num % m

        if num + rests[m-index] > max_sum and rests[m-index] > num:
            max_sum = num + rests[m-index]
            l = rests[m - index]
            r = num
        if num > rests[index]:
            rests[index] = num
    print(l, r)
            
def main():
    #bruteforce()
    optimal()

main()
