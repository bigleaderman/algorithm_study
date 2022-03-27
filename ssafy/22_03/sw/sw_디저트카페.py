def dfs(n, ci, cj, v):
    global ans
    if n==2 and ans >= len(v)*2:
        return
    if n > 3:   #종료조건
        return
    if n == 3 and ci == i and cj == j and ans < len(v):
        ans = len(v)
        return

    for k in range(n, n+2):
        ni, nj = ci + di[k], cj + dj[k]
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] not in v:
            v.append(arr[ni][nj])
            dfs(k, ni, nj, v)
            v.pop()


di, dj = (1, 1, -1, -1, 1), (-1, 1, 1, -1, -1)
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = -1
    for i in range(0, N-2):
        for j in range(1, N-1):
            dfs(0, i, j, [])
    print(f'#{tc} {ans}')