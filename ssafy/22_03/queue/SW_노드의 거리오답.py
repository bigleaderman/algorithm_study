def bfs(now, cnt):
    # asw값은 전역변수
    global asw
    # n은 arr의 idx로 사용하기 위해서 사용 항상 idx 0은 0이므로 1부터 시작하기
    # visited[now]가 0이여야 방문하지 않았다는 것이다.
    # arr[now]에서 길이가 n이 될때까지 돌기
    # 방문 체크
    visited[now] = 1
    for i in range(1, len(arr[now])):
        # 갈 노드를 go로 지정
        go = arr[now][i]
        # 출발지와 목적지가 같고 cnt 값이 이전 asw값보다 작을 경우 asw 수정
        if go == G:
            if asw > cnt:
                asw = cnt
            return
        # 방문 체크
        visited[now] = 1
        # 갈 노드가 방문 하지 않았을 때 재귀
        if not visited[go]:
            bfs(go, cnt + 1)
            # 방문 체크 복귀
            visited[now] = 0


# 입력값 받기
for tc in range(1, int(input()) + 1):
    V, E = map(int, input().split())
    # arr에 노드 시작점과 끝점을 받기
    arr = [[0] for _ in range(V+1)]
    # arr 각 위치에 노드 시작점과 끝점 받아오기
    for i in range(E):
        s, g = map(int, input().split())
        arr[s].append(g)
        arr[g].append(s)
    # 방문한지 안한지 체크
    visited = [0] * (V + 1)
    S, G = map(int, input().split())
    # 최솟값이 되는 asw 찾기
    asw = 1000
    # dfs로 start에서부터 cnt하면서 돌기
    bfs(S, 1)
    # asw이 초기값과 같으면 노드가 이어지지 않았으므로 asw은 1000
    if asw == 1000:
        print(f'#{tc} {0}')
    else:
        print(f'#{tc} {asw}')


