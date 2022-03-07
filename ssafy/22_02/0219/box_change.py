for tc in range(int(input())):
    print(f'#{tc+1}', end=' ')
    N, Q = map(int, input().split())
    num_list = [0] * N
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L, R+1):
            num_list[j-1] = i
    for k in range(N):
        print(num_list[k], end=' ')
    print()