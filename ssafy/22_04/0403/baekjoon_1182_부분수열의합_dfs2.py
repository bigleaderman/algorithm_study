from sys import stdin

def dfs(k, v):
    global cnt
    if k >= 1 and v == S:
        cnt += 1
    for i in range(k, N):
        if not visited[i]:
            visited[i] = 1
            dfs(i+1, v+lst[i])
            visited[i] = 0

N, S = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
cnt = 0
visited=[0] * N
dfs(0,0)
print(cnt)