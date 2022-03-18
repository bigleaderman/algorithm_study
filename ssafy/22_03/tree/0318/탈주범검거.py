import sys
sys.stdin = open('탈주범검거.txt', 'r')

# hall의 value를 delta의 idx로 이용해서 이동을 한다.
delta = [[-1, 0], [1, 0], [0, -1], [0, 1]]  #상하좌우
hall = [[0], [0, 1, 2, 3], [0, 1], [2, 3], [0, 3], [1, 3], [1, 2], [0, 2]]

for tc in range(1, int(input()) + 1):
    N, M, R, C, L = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 방문 처리를 해서 방문한 곳이 강도가 있을 수 있는 곳이다.
    visited = [[0] * M for _ in range(N)]
    # Q의 3번째 인덱스에 몇시간 지났는지 카운트
    Q = [[R, C, 1]]
    # queue를 이용해서 cnt의 임계치 까지 이동한다.
    while Q:
        now = Q.pop(0)
        y, x = now[0], now[1]
        visited[y][x] = 1
        # 시간이 3시간이 됬으면 더 이상 이동하지 못하도록한다.
        if now[2] == L:
            continue
        now_value = lst[y][x]
        now_hall = hall[now_value]
        # 홀의 값들을 이용해서 delta 이동을한다
        for i in now_hall:
            di, dj = delta[i]
            # 지금 y, x를 찾는다.
            new_y, new_x = y + di, x + dj
            # 범위 내에 있어야하고 value값이 0이 아니여야한다.
            if 0 <= new_y < N and 0 <= new_x < M and lst[new_y][new_x] and not visited[new_y][new_x]:
                new_value = lst[new_y][new_x]
                new_hall = hall[new_value]
                # 이 조건식은 현재 이동할려는 방식에 따라서 그위치가 연결되어 있는지 확인하는 것이다.
                if i == 0 and 1 in new_hall:
                    Q.append([new_y, new_x, now[2] + 1])
                elif i == 1 and 0 in new_hall:
                    Q.append([new_y, new_x, now[2] + 1])
                elif i == 2 and 3 in new_hall:
                    Q.append([new_y, new_x, now[2] + 1])
                elif i == 3 and 2 in new_hall:
                    Q.append([new_y, new_x, now[2] + 1])

    total = 0
    for i in range(N):
        total += sum(visited[i])
    print(f'#{tc} {total}')
