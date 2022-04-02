from collections import deque

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())

    visited = [False] * 1000001

    queue = deque()
    queue.append((N, 0))
    visited[N] = True

    while queue:
        now, count = queue.popleft()
        if now == M:
            print(f'#{tc} {count}')
            break

        if now + 1 <= 1000000 and not visited[now + 1]:
            queue.append((now + 1, count + 1))
            visited[now + 1] = True

        if 0 <= now - 1 and not visited[now - 1]:
            queue.append((now - 1, count + 1))
            visited[now - 1] = True

        if now + 2 <= 1000000 and not visited[now * 2]:
            queue.append((now * 2, count + 1))
            visited[now * 2] = True

        if 0 <= now - 10 and not visited[now - 10]:
            queue.append((now - 10, count + 1))
            visited[now - 10] = True
