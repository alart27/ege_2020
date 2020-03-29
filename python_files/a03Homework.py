def array_input_many_strings(n):
    a = []
    for i in range (len(a)):
        new_element = int(input())
        a.append(new_element)

    return a

def array_input_one_string():
    return list(map(int, input().split()))
    

#def arrayOutput(*a):
#	for i in range (len(a)):
#		print (a[i])


def array_output(a):
    print(' '.join(map(str, a)))


def array_sum(a):
    summa = 0
    for n in a:
        summa = summa + n
    return summa

def array_mean(a):
    return array_sum(a)/len(a)


if __name__ == '__main__':        
    a = [1, 3, 4, 5]
    a = array_input_one_string()
    array_output(a)
    print(array_mean(a))


