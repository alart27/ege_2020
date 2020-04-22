"""
ex from school archive
"""

n = int(input())
pairs = 0
m = 80
b = 50
smaller_or_50 = [0 for i in range(m)]
bigger_50 = [0 for i in range(m)]


for i in range(n):
    number = int(input())
    if number > 50:
        pairs += bigger_50[(m - number%m)%m] + smaller_or_50[(m - number % m) % m]
        bigger_50[number % m] += 1
    else:
        pairs += bigger_50[(m - number%m)%m]
        smaller_or_50[number % m] += 1

print(pairs)
