for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    for _ in range(M):
        lst.append(lst.pop(0))
    print(f'#{tc} {lst[0]}')
