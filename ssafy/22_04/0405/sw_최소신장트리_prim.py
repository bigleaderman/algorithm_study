for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    tree = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        tree[n1].append([n2, w])
        tree[n2].append([n1, w])
    weights = [98765] * (V+1)
    weights[0] = 0
    check = [0] * (V+1)
    cnt = 0
    sequence = 0
    while V >= sequence:
        min_weight = 98764
        for i in range(V+1):
            if min_weight > weights[i]:
                if not check[i]:
                    min_weight = weights[i]
                    min_idx = i
        cnt += weights[min_idx]
        check[min_idx] = 1
        for n, w in tree[min_idx]:
            if weights[n] > w:
                weights[n] = w
        sequence += 1
    print(f'#{tc} {cnt}')