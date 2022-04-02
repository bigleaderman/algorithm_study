# 재귀를 이용해서 N에 도착할 때 까지 찾기
def f(now, value):
    global min_value

    if value > min_value:
        return
    if now == N:
        if min_value > value:
            min_value = value
    else:
        for i in range(N+1):
            if arr[now][i]:
                f(i, value + arr[now][i])

for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    arr = [[0] * (N+1) for _ in range(N+1)]
    min_value = 9999999
    for _ in range(E):
        # arr[s][e]에 value를 넣어주기
        s, e, v = map(int, input().split())
        arr[s][e] = v
    f(0, 0)
    print(f'#{tc} {min_value}')
