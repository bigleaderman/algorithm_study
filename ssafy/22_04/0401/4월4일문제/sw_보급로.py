import sys
from sys import setrecursionlimit
sys.stdin = open('보급로.txt', 'r')
limit = 10 ** 10
setrecursionlimit(limit)

def f(i, j, v): # 현재 위치와 value값 넘겨주기
    visited[i][j] = v

    if (i, j) == (N-1, N-1):
        return
    for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ni, nj = i + x, j + y
        if 0 <= ni < N and 0 <= nj < N:
            new_value = v + arr[ni][nj]
            if new_value < visited[ni][nj]:
                f(ni, nj, new_value)


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[9*100*50]*N for _ in range(N)]
    f(0, 0, arr[0][0])
    print(f'#{tc} {visited[N-1][N-1]}')