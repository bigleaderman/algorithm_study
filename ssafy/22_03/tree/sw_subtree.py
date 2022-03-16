for tc in range(1, int(input())+1):
    E, N = map(int, input().split())
    tree = [[0] for _ in range(E + 2)]  #노드 번호는 E+1이고 시작이 1이므로 E+2를 반복으로 돌린다.
    #이미 N이 있을때 부터 1이므로 cnt = 1
    cnt = 1

    # tree 만들기, 0은 제외시켜주기
    lst = list(map(int, input().split()))
    for i in range(0, len(lst), 2):
        tree[lst[i]].append(lst[i+1])

    # N 가지들을 stack에 넣기
    stack = []
    for x in tree[N]:
        if x:
            stack.append(x)
    # stack이 끝날때가 자손이 끝날 때이미로 while문 돌기
    while stack:
        idx = stack.pop(-1)
        cnt += 1    # 돌때 마다 자손수 추가
        for x in tree[idx]: # 이어서 자손들 파악하기
            if x:
                stack.append(x)
    print(f'#{tc} {cnt}')
