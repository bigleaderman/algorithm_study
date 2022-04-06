for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    tree = [list(map(int, input().split())) for _ in range(E)]
    tree.sort(key=lambda x : x[2])
    check = [0] * (V+1)
    cnt = 0
    n = 0
    i = 0
    while n != V:
        if not check[tree[i][0]] or not check[tree[i][1]]:
            check[tree[i][0]] = 1
            check[tree[i][1]] = 1
            cnt += tree[i][2]
            n += 1
        i += 1
    print(f'#{tc} {cnt}')
