

# 문제 설명이 굉장히 어렵게 되있다. 어떻게 문제만 보고 이해하라는건지...
# 예제를 다 그려보고 숫자간의 깊이가 4가 될수 잇는 것을 찾으라고 하는것 같다.
# 구현은 인접리스트를 만든다.
# 어디서 출발 했을 때 깊이가 4가 될지 모르니 완전탐색을 한다.
# dfs 요소에 cnt를 줘서 cnt가 4 즉 깊이가 4인 갚을 찾도록 한다.
from sys import stdin

def dfs(s, cnt):
    global flag
    if flag:
        return
    if cnt == 4:
        flag = 1
        return
    for ni in friends[s]:
        if not visited[ni]:
            visited[ni] = 1
            dfs(ni, cnt+1)
            visited[ni] = 0

N, M = map(int, stdin.readline().split())
friends = [[] for _ in range(N)]
flag = 0
for _ in range(M):
    v1, v2 = map(int, stdin.readline().split())
    friends[v1].append(v2)
    friends[v2].append(v1)
for i in range(N):
    visited = [0] * N
    visited[i] = 1
    if not flag:
        dfs(i, 0)
print(1 if flag else 0)
