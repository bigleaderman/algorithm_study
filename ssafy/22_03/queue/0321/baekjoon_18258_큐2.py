from sys import stdin
from collections import deque

N = int(stdin.readline())
Q = deque()
for _ in range(N):
    order = stdin.readline().split()
    if order[0] == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)

    elif order[0] == 'size':
        print(len(Q))

    elif order[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)

    elif order[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)

    elif order[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)

    else:
        Q.append(order[1])
