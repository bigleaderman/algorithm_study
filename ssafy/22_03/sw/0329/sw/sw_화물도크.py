for tc in range(1, int(input()) + 1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort()
    subset = [[] for _ in range(2 ** N)]
    max_cnt = 0
    # 부분 집합을 subset안에 다 넣기
    for i in range(1 << len(lst)):
        for j in range(len(lst)):
            if i & (1 << j):
                print(lst[j], end=' ')
                subset[i].append(lst[j])
        print()
    print(subset)
    for sub in subset:
        flag = 0
        for i in range(len(sub)-1):
            if flag:
                break
            for j in range(i+1, len(sub)):
                if sub[i][1] > sub[j][0]:
                    flag = 1
                    break
        if not flag:
            if max_cnt < len(sub):
                max_cnt = len(sub)
    print(f'#{tc} {max_cnt}')