from sys import stdin

N = int(stdin.readline())
front = 0
rear = N
Q = list(range(1, N + 1)) + [0] * 2 * N
while rear - front != 1:
    front += 1
    Q[rear] = Q[front]
    front += 1
    rear += 1
print(Q[front])