from sys import stdin
import sys
sys.setrecursionlimit(1000000)
def find_par(n):
    lst = tree[n]
    stack = []
    visited[n] = 1
    for idx in lst[1:]:
        if not visited[idx]:
            visited[idx] = 1
            stack.append(idx)
    for idx in stack:
        par[idx] = n
        find_par(idx)

N = int(stdin.readline())
tree = [[0] for _ in range(N+1)]
par = [0] * (N + 1)
visited = [0] * (N + 1)
for i in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

find_par(1)
for value in par[2:]:
    print(value)