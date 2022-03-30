
for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [list(map(int, input().split()))[::-1] for _ in range(N)]
    lst = sorted(lst)
    # lst의 끝나는 시간보다 시작하는시간이 큰 시간일 때 까지 찾기
    now = 0
    k = 1
    cnt = 1
    while k != N:
        if lst[now][0] <= lst[k][1]:
            now = k
            k += 1
            cnt += 1
        else:
            k += 1
    print(f'#{tc} {cnt}')