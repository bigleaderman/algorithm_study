for tc in range(1, int(input())+1):
    n = int(input())
    check = [1] + [0] * (n-1)
    back = [sorted(list(map(int, input().split()))) for _ in range(n)]
    for i in range(n):
        if back[i][0] % 2 == 0:
            back[i][0] -= 1
        if back[i][1] % 2:
            back[i][1] += 1
    for j in range(n):
        for k in range(j+1, n):
            if back[j][0] <= back[k][0] <= back[j][1] or back[j][0] <= back[k][1] <= back[j][1] \
                    or back[k][0] <= back[j][1] <= back[k][1] or back[k][0] <= back[j][0] <= back[k][1]:
                check[k] = 1

    print(f'#{tc} {sum(check)}')
