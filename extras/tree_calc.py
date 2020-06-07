
# можно сделать проще структуру, но код будет чуть сложнее

# tree = [op, left, right]
# tree = [3]

def calc(tree):
    if len(tree) == 1:
        return tree[0]
    else:
        op = tree[0]
        left = tree[1]
        right = tree[2]
        if op == '+':
            return calc(left) + calc(right)
        elif op == '*':
            return calc(left) * calc(right)

trees = [
    ['+', [3], [5]],               # 3 + 5
    ['*', [2], ['+', [3], [5]]],   # 2 * (3 + 5)
    ['+', [5], ['*', [2], [3]]],   # 5 + 2 * 3
]

for tree in trees:
    print(tree, '->', calc(tree))


