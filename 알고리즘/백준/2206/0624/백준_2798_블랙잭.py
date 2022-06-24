from sys import stdin

def dfs(n, i, total):
    global max_num
    if total > M:
        return
    if n == 3:
        if total > max_num:
            max_num = total

    else:
        for j in range(i, N):
            dfs(n+1, j+1, total + lst[j])



N, M = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
max_num = 0

for i in range(N-2):
    dfs(1, i+1, lst[i])

print(max_num)