import sys
from collections import deque
sys.stdin = open('offer.txt','r')

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for tc in range(1, int(input()) + 1):
    n = int(input())
    lst = [list(map(int, input())) for _ in range(n)]
    visited = [[810000] * n for _ in range(n)]
    visited[0][0] = 0
    stack = deque()
    stack.append((0,0))
    while stack:
        y, x = stack.popleft()
        for k in range(4):
            dy, dx = delta[k][0], delta[k][1]
            b, a = y + dy, x + dx
            if 0 <= b <= n - 1 and 0 <= a <= n - 1:
                if visited[y][x] + lst[y][x] < visited[b][a]:
                    visited[b][a] = visited[y][x] + lst[y][x]
                    stack.append([b, a])
    print(f'#{tc}', visited[n-1][n-1])