"""
Дан список чисел.
Определите, сколько в этом списке элементов,
которые больше двух своих соседей и выведите количество таких элементов. 
"""

def strong_elements(array):

    count = 0
    
    for i in range(1, len(array)-1):
        if array[i-1] < array[i] and array[i] > array[i+1]:
            count +=1

    print(count)


def main():
    a = [int(word) for word in input().split()]
    strong_elements(a)


main()
