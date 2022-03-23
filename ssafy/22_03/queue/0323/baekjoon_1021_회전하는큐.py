from sys import stdin
from  collections import deque

N, M = map(int, stdin.readline().split())
lst = list(map(int, input().split()))
Q = deque(range(1, N + 1))
target = 0
cnt = 0
while target != M:
    right = Q.index(lst[target])
    left = len(Q) - Q.index((lst[target]))
    # target이 최소 회전하여 idx 0으로 올 수 있도록하고 최소회전수 cnt 더하기.
    if right >= left:
        Q.rotate(left)
        cnt += left
    else:
        Q.rotate(-right)
        cnt += right
    # 위치가 됬을 때 pop하고 target수 1 늘리기.
    Q.popleft()
    target += 1
print(cnt)




