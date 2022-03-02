for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    for i in range(E):  #양방향 노드를 다 받기 위해서 뒤집어서 append하기
        arr.append([arr[i][1], arr[i][0]])
    s, e = map(int, input().split())
    visited = [0]*(V+1) #방문을 확인하기 위해서 vistied변수 설정
    stack = [[s, 0]]    #간선 방문 횟수를 확인 하기 위해서 stack 뒤에 0 value 추가
    cnt = 0 #노드의 방문 횟수
    while stack:    #BFS를 이용하여 도착지 올때 까지 반복
        s = stack.pop(0)
        visited[s[0]] = 1
        if visited[e] == 1:
            cnt = s[1]
            break
        for x, y in arr:
            if s[0] == x and not visited[y]:
                stack.append([y, s[1] + 1])
    print(f'#{tc} {cnt}')