N, K = map(int, input().split())
lst = list(range(1, N + 1)) + [0] * (N * 3)
front, rear = 0, N
answer = []
while rear != front:
    for _ in range(K-1):
        lst[rear] = lst[front]
        rear, front = rear + 1, front + 1
    answer.append(lst[front])
    front += 1
print(answer)


