from sys import stdin

def dfs(k, v):
    global cnt

    if k >= N:
        return
    v += lst[k]
    if v == S:
        cnt += 1
    dfs(k+1, v-lst[k])
    dfs(k+1, v)

N, S = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
cnt = 0
dfs(0,0)
print(cnt)