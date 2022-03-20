from sys import stdin


N = int(stdin.readline())
tree = [[0] for _ in range(N+1)]
par = [0] * (N + 1)
visited = [0] * (N + 1)
# 트리를 그래프처럼 받아온다.
for i in range(N-1):
    n1, n2 = map(int, input().split())
    tree[n1].append(n2)
    tree[n2].append(n1)

# 그러고 Queue를 이용해 전체 순회하고 방문안했던 곳을 찾는다.
Q = [1]
visited[1] = 1
while Q:
    now = Q.pop(0)
    now_c = tree[now][1:]
    for idx in now_c:
        if not visited[idx]:
            visited[idx] = 1
            par[idx] = now
            Q.append(idx)

for value in par[2:]:
    print(value)
