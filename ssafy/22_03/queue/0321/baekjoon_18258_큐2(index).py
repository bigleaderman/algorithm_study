from sys import stdin

N = int(stdin.readline())
Q = [0] * N
front = rear = 0
for _ in range(N):
    order = stdin.readline().split()
    if order[0] == 'pop':
        if rear != front:
            print(Q[front])
            front += 1
        else:
            print(-1)

    elif order[0] == 'size':
        print(rear - front)

    elif order[0] == 'empty':
        if rear != front:
            print(0)
        else:
            print(1)

    elif order[0] == 'front':
        if rear != front:
            print(Q[front])
        else:
            print(-1)

    elif order[0] == 'back':
        if rear != front:
            print(Q[rear-1])
        else:
            print(-1)

    else:
        Q[rear] = order[1]
        rear += 1
