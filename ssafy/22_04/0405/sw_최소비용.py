def bfs():
    Q = [[0, 0]]
    front = 0
    rear = 1
    while rear != front:
        i, j = Q[front]
        front += 1
        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i + x, j + y
            if 0 <= ni < N and 0 <= nj < N:
                if arr[ni][nj] > arr[i][j]:
                    new_cost = visited[i][j] - arr[i][j] + arr[ni][nj] + 1
                else:
                    new_cost = visited[i][j] + 1
                if visited[ni][nj] > new_cost:
                    visited[ni][nj] = new_cost
                    Q.append([ni, nj])
                    rear += 1

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[987654] * N for _ in range(N)]
    visited[0][0] = 0
    bfs()
    print(f'#{tc} {visited[N-1][N-1]}')