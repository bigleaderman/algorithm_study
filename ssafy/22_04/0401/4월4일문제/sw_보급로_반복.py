import sys
from collections import deque
sys.stdin = open('보급로.txt', 'r')

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    visited = [[9*100*50]*N for _ in range(N)]
    visited[0][0] = arr[0][0]
    stack = deque([[0, 0]])
    while stack:
        now = stack.popleft()
        i, j = now[0], now[1]
        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            ni, nj = i + x, j + y
            if 0 <= ni < N and 0 <= nj < N:
                new_value = visited[i][j] + arr[ni][nj]
                if new_value < visited[ni][nj]:
                    stack.append([ni, nj])
                    visited[ni][nj] = new_value
    print(f'#{tc} {visited[N-1][N-1]}')