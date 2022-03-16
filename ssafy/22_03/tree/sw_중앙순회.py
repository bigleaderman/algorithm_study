
def in_order(node):
    if node:
        in_order(tree[node][1])
        print(tree[node][0], end='')
        in_order(tree[node][2])


for tc in range(1, 11):
    n = int(input())
    arr = [0] + [list(input().split()) for _ in range(n)]
    tree = [[0] * 3 for _ in range(n+1)]
    stack = []
    for i in range(1, n+1):
        if len(arr[i]) == 2:
            tree[int(arr[i][0])][0] = arr[i][1]
        elif len(arr[i]) == 3:
            tree[int(arr[i][0])][0] = arr[i][1]
            if int(arr[i][0]) * 2 == int(arr[i][2]):
                tree[int(arr[i][0])][1] = int(arr[i][2])
            else:
                tree[int(arr[i][0])][2] = int(arr[i][2])
        else:
            tree[int(arr[i][0])][0] = arr[i][1]
            tree[int(arr[i][0])][1] = int(arr[i][2])
            tree[int(arr[i][0])][2] = int(arr[i][3])
    print(f'#{tc}', end=' ')
    in_order(1)
    print()