


from sys import stdin

def bfs(i, j):
    Q = [[i, j]]
    front = 0
    rear = 1
    while front != rear:
        ni, nj = Q[front]
        front += 1
        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nni, nnj = ni + x, nj + y
            if 0 <= nni < N and 0 <= nnj < M and arr[nni][nnj] == '1' and visited[nni][nnj] > visited[ni][nj] + int(arr[ni][nj]):
                visited[nni][nnj] = visited[ni][nj] + int(arr[ni][nj])
                rear += 1
                Q.append([nni, nnj])

N, M = map(int, stdin.readline().split())
arr = [list(stdin.readline().strip()) for _ in range(N)]
visited = [[999]*M for _ in range(N)]
visited[0][0] = 1
bfs(0, 0)
print(visited[N-1][M-1])