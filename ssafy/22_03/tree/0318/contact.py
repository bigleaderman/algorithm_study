for tc in range(1, 2):
    N, S = map(int, input().split())
    visited = [0] * 101
    lst = [[0] for _ in range(101)]
    phone = list(map(int, input().split()))
    for i in range(N//2):
        lst[phone[i * 2]].append(phone[i * 2 + 1])

    last = 1
    Q = []
    for i in lst[S]:
        if i:
            Q.append([i, 1]) # 왼쪽 value 오른쪽 cnt
            visited[i] = 1

    node = []
    while Q:
        now = Q.pop(0)
        value = now[0]
        cnt = now[1]
        visited[value] = cnt
        if cnt > last:
            last = cnt
        for v in lst[value][1:]:
            if not visited[v]:
                Q.append([v, now[1] + 1])
                visited[v] = now[1] + 1
    print(f'# {tc}', 100 - visited[::-1].index(last))