for tc in range(1, int(input()) + 1):
    n = int(input())
    num_list = []
    for i in range(1, n+1):
        num_list.append([1]*i)
    for j in range(2, n):
        for k in range(1,j):
            num_list[j][k] = num_list[j-1][k-1] + num_list[j-1][k]
    print(f'#{tc}')
    for a in num_list:
        print(*a, end=' ')
        print()
