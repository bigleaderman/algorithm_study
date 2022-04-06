from sys import stdin

# 인접리스트를 이용, 그리고 인접리스트 하나씩 sort를 이용해서 정렬
# dfs, bfs 구현한뒤에 순서대로 리스트에 넣어서 출력
def dfs(s):
    for i in lst[s]:
        if not visited_dfs[i]:
            visited_dfs[i] = 1
            DFS.append(i)
            dfs(i)

def bfs(s):
    Q = [s]
    front = 0
    rear = 1
    while front != rear:
        i = Q[front]
        front += 1
        for ni in lst[i]:
            if not visited_bfs[ni]:
                visited_bfs[ni] = 1
                Q.append(ni)
                BFS.append(ni)
                rear += 1

N, M, S = map(int, stdin.readline().split())
lst = [[] for _ in range(N+1)]
visited_dfs = [0] * (N+1)
visited_bfs = [0] * (N+1)
DFS = [S]
BFS = [S]
for _ in range(M):
    v1, v2 = map(int, stdin.readline().split())
    lst[v1].append(v2)
    lst[v2].append(v1)
for i in range(1, N+1):
    lst[i].sort()
visited_dfs[S] = 1
visited_bfs[S] = 1
dfs(S)
print(*DFS)
bfs(S)
print(*BFS)
