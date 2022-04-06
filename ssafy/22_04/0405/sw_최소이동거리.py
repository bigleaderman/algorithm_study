for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    visited = [999] * (N+1)
    visited[0] = 0
    for i in range(E):
        s, e, w = map(int, input().split())
        if visited[e] > visited[s] + w:
            visited[e] = visited[s] + w
    print(f'#{tc} {visited[N]}')