import sys
sys.stdin = open('pinball.txt', 'r')

for tc in range(1, int(input())+1):
    N = int(input())
    # 리스트 받아오기, 벽 맞으면 튕겨 나와야 하기 때문에 180도로 바뀌는 조건인 블록 5를 둘러싼다.
    lst = [[5] * (N + 2)]+ [[5] + list(map(int, input().split())) + [5] for _ in range(N)] + [[5] * (N + 2)]
    # 델타를 이용해서 블록을 움직인다.
    delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    # change를 이용하여 각 위치에 도착했을 때 방향 변경 혹은 이동할 수 있도록 한다.
    change = [
        [],
        [2, 0, 3, 1],   #1
        [1, 2, 3, 0],   #2
        [1, 3, 0, 2],   #3
        [3, 0, 1, 2],   #4
        [1, 0, 3, 2],   #5
        [], #6
        [], #7
        [], #8
        [], #9
        []  #10
    ]
    # 웜홀 파악하기
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if 6 <= lst[i][j] <= 10:
                change[lst[i][j]].append([i, j])
    max_cnt = 0
    # 전체 위치와 전체 방향을 다 탐색하기
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if lst[i][j]:
                continue
            for k in range(4):
                cnt = 0
                # 처음 위치를 a,b 변수로 두고, 방향 이동 위치를 어떻게 할 지 결정한다.
                move = k
                a, b = i, j
                # 블랙홀이나 자기 위치를 만나기전 까지는 계속 반복한다.
                while True:
                    # 다음 방향으로 이동한다.
                    a, b = a + delta[move][0], b + delta[move][1]
                    # 블랙홀이나 처음 위치를 만났을 때 게임을 끝낸다.
                    if [a, b] == [i, j] or lst[a][b] == -1:
                        if cnt > max_cnt:
                            max_cnt = cnt
                        break
                    # 블록일 때
                    elif 1 <= lst[a][b] <= 5:
                        # move를 change에서 현재 몇번 블록이고 현재 방향이 어떻냐에 따라서 방향을 변경한다.
                        move = change[lst[a][b]][move]
                        cnt += 1
                    # 웜홀을 만났을 때
                    elif 6 <= lst[a][b] <= 10:
                        # 위치를 다른 웜홀 위치로 이동시켜준다.
                        if [a, b] == change[lst[a][b]][0]:
                            [a, b] = change[lst[a][b]][1]
                        else:
                            [a, b] = change[lst[a][b]][0]

    print(f'#{tc} {max_cnt}')
