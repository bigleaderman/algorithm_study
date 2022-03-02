for tc in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]  #delta를 이용하여 list 이동

    for i in range(N):  #start와 end 찾기
        for j in range(N):
            if arr[i][j] == 2:
                s = [i, j, 0]   #start에는 idx 2에 이동한 숫자를 count하기 위하여 0 value 넣기
            elif arr[i][j] == 3:
                e = [i, j]
                arr[i][j] = 0
    stack = [s]
    cnt = 0
    while stack:    #stack이 없을 때 까지 반복하기
        s = stack.pop(0)    #BFS사용을 위하여 pop(0)이용
        arr[s[0]][s[1]] = 1 #방문한곳은 1로 변경
        if s[0:2] == e: #도착지를 찾았을 때 cnt요소를 이때 동안 이동한 횟수 -1하기
            cnt = s[2] - 1
        for x, y in delta:  #delta 이동 할 때 이동할려는 곳이 범위 안에 있고 value 값이 0 일때 stack에 append
            if 0 <= s[0] + x < N and 0 <= s[1] + y < N and arr[s[0] + x][s[1] + y] == 0:
                stack.append([s[0] + x, s[1] + y, s[2] + 1])

    print(f'#{tc} {cnt}')
