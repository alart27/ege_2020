"""
informatics 64

print elements with even indecies
"""

n = int(input())
numbers = [int(word) for word in input().split()]

for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i], end=' ')

#for i in range(0, len(numbers), 2):
#    print(numbers[i], end=' ')


### get it shorter
#input()
#print(' '.join(input().split()[::2]))
