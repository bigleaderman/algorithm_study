from sys import stdin

# 섬의 갯수와 비슷함
# 전체 인접리스트를 돌면서 stack을 이용한 dfs를 한다.
# 인접해 있으면 방문하고 방문 처리한다
# 그래도 방문 안한곳 파악을 하는 것을 반복하면서 cnt를 증가시켜 준다
N, M = map(int, stdin.readline().split())
lst = [[] for _ in range(N+1)]
visited = [0] * (N + 1)
cnt = 0
for _ in range(M):
    v1, v2 = map(int, stdin.readline().split())
    lst[v1].append(v2)
    lst[v2].append(v1)
for i in range(1, N+1):
    if not visited[i]:
        cnt += 1
        stack = [i]
        visited[i] = 1
        while stack:
            ni = stack.pop()
            for j in lst[ni]:
                if not visited[j]:
                    visited[j] = 1
                    stack.append(j)
print(cnt)