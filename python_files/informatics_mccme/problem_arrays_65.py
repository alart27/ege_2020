"""
informatics 65

count number of positive elements
"""

n = input()
numbers = [int(word) for word in input().split()]

counter = 0
for number in numbers:
    if number > 0:
        counter += 1

print(counter)
