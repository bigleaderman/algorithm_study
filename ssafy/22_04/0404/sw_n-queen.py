def dfs(i):
    global cnt
    if i == N:
        cnt += 1
    else:
        for j in range(N):
            if not visited[i][j]:
                for k in [1, -1]:
                    ni, nj = i, j
                    while 0 <= ni < N:
                        if not visited[ni][j]:
                            visited[ni][j] = i + 1
                        ni += k
                    ni, nj = i, j
                    while 0 <= nj < N and 0 <= ni < N:
                        if not visited[ni][nj]:
                            visited[ni][nj] = i + 1
                        ni, nj = ni + k, nj + k
                    ni, nj = i, j
                    while 0 <= nj < N and 0 <= ni < N:
                        if not visited[ni][nj]:
                            visited[ni][nj] = i + 1
                        ni, nj = ni - k, nj + k
                dfs(i+1)
                for k in [1, -1]:
                    ni, nj = i, j
                    while 0 <= ni < N:
                        if visited[ni][j] == i + 1:
                            visited[ni][j] = 0
                        ni += k
                    ni, nj = i, j
                    while 0 <= nj < N and 0 <= ni < N:
                        if visited[ni][nj] == i + 1:
                            visited[ni][nj] = 0
                        ni, nj = ni + k, nj + k
                    ni, nj = i, j
                    while 0 <= nj < N and 0 <= ni < N:
                        if visited[ni][nj] == i + 1:
                            visited[ni][nj] = 0
                        ni, nj = ni - k, nj + k



for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    dfs(0)
    print(f'#{tc} {cnt}')

