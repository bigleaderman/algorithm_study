
for tc in range(1, int(input()) + 1):
    N, E = map(int, input().split())
    vistied = [0] + [98765] * (N)
    for _ in range(E):
        # arr[s][e]에 value를 넣어주기
        s, e, v = map(int, input().split())
        if vistied[e] > vistied[s] + v:
            vistied[e] = vistied[s] + v
    print(f'#{tc} {vistied[N]}')