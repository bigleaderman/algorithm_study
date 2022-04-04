
def f(i, j, k, v):
    global cnt
    if 7 - k + v < 4:
        return
    if k == 7:
        print(i, j)
        cnt += 1/v
    else:
        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i+x, j+y
            if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                visited[ni][nj] = 1
                f(ni, nj, k+1, v+1 if arr[ni][nj] == 'S' else v)
                visited[ni][nj] = 0

arr = [list(input()) for _ in range(5)]
S_site = []
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            S_site.append([i, j])
cnt = 0
for i, j in S_site:
    visited = [[0] * 5 for _ in range(5)]
    print(i, j)
    f(i, j, 1, 1)
print(cnt)
