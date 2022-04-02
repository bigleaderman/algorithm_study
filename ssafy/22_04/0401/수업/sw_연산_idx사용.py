
def bfs(n):
    Q = [[n, 0]]
    visited[n] = 1
    front = 0
    rear = 1
    while front <= rear:
        now = Q[front]
        front += 1
        value, cnt = now[0], now[1]
        if value == target:
            return cnt
        for plus in [1, -1, -10]:
            new_value = value + plus
            if 1000000 >= new_value > 0 and not visited[new_value]:
                Q.append([new_value, cnt+1])
                rear += 1
                visited[new_value] = 1
        new_value = value * 2
        if 1000000 >= new_value > 0 and not visited[new_value]:
            Q.append([new_value, cnt+1])
            rear += 1
            visited[new_value] = 1


for tc in range(1, int(input()) + 1):
    num, target = map(int, input().split())
    cnt = 0
    visited = [0] * 1000001
    print(f'#{tc} {bfs(num)}')