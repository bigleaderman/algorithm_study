from sys import stdin
from collections import deque
N = int(stdin.readline())
Q = deque([[N, 0]])
while Q:
    value, cnt = Q.popleft()
    if value == 1:
        min_cnt = cnt
        break
    else:
        if not value % 3:
            Q.append([value//3, cnt+1])
        if not value % 2:
            Q.append([value//2, cnt+1])
        Q.append([value-1, cnt+1])

print(min_cnt)
