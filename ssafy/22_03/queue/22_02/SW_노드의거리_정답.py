for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    for i in range(E):
        arr.append([arr[i][1], arr[i][0]])
    s, e = map(int, input().split())
    visited = [0]*(V+1)
    stack = [[s, 0]]
    cnt = 0
    while stack:
        s = stack.pop(0)
        visited[s[0]] = 1
        if visited[e] == 1:
            cnt = s[1]
            break
        for x, y in arr:
            if s[0] == x and not visited[y]:
                stack.append([y, s[1] + 1])
    print(f'#{tc} {cnt}')