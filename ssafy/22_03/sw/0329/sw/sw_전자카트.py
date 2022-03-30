def f(s, k, v):  # n은 크기, s는 출발지점, k는 깊이, v는 value값
    global min_value
    if v > min_value:
        return

    elif k == N - 1:
        v += arr[s][0]
        if min_value > v:
            min_value = v

    else:
        for i in range(1, N):
            if not visited[i]:
                visited[i] = 1
                f(i, k + 1, v + arr[s][i])
                visited[i] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_value = 10000
    f(0, 0, 0)
    print(f'#{tc} {min_value}')