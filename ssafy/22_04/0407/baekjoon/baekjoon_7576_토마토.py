from sys import stdin

def bfs(rear):
    front = 0
    max_value = 0
    while rear != front:
        i, j, cnt = Q[front]
        front += 1
        max_value = max(cnt, max_value)
        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i + x, j + y
            if 0 <= ni < N and 0 <= nj < M and not arr[ni][nj]:
                arr[ni][nj] = 1
                rear += 1
                Q.append([ni, nj, cnt + 1])
    return max_value


M, N = map(int, stdin.readline().split())
arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
Q = []
rear = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            Q.append([i, j, 0])
            rear += 1
min_value  = bfs(rear)
flag = 1
for i in range(N):
    if flag:
        for j in range(M):
            if not arr[i][j]:
                flag = 0
                break
print(min_value if flag else -1)