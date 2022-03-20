from sys import stdin

# 트리 1부터 시작해서 반복문을 돌면서 left, right idx를 자식의 value값과 tree[i][0]의 value값을 비교해 찾았다.
def pre_order(n):
    lst = tree[n]
    print(lst[0], end='')
    for i in range(N):
        if lst[1] == tree[i][0]:
            left = i
        if lst[2] == tree[i][0]:
            right = i
    if tree[n][1] != '.':
        pre_order(left)
    if tree[n][2] != '.':
        pre_order(right)

def in_order(n):
    lst = tree[n]
    for i in range(N):
        if lst[1] == tree[i][0]:
            left = i
        if lst[2] == tree[i][0]:
            right = i
    if tree[n][1] != '.':
        in_order(left)
    print(lst[0], end='')
    if tree[n][2] != '.':
        in_order(right)

def poster_order(n):
    lst = tree[n]
    for i in range(N):
        if lst[1] == tree[i][0]:
            left = i
        if lst[2] == tree[i][0]:
            right = i
    if tree[n][1] != '.':
        poster_order(left)
    if tree[n][2] != '.':
        poster_order(right)
    print(lst[0], end='')

# tree를 있는 그대로 순서대로 받아왔다
N = int(stdin.readline())
tree = [list(stdin.readline().split()) for _ in range(N)]
pre_order(0)
print()
in_order(0)
print()
poster_order(0)