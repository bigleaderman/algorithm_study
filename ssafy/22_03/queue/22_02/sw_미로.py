import sys
sys.stdin = open('miro.txt', 'r')

# delta를 이용해서 이동
delta = [[1, 0], [-1, 0], [0, -1], [0, 1]]


for tc in range(1, 11):
    # 입력값 받아오기
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    # 출발지점 찾기
    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start = (i, j)
    # 도착지를 찾음을 판단하는 config
    config = 0
    # 출발지에 push
    stack = [start]
    # stack이 끝날 때 까지 반복
    while stack:
        # bfs 사용하기
        x, y = stack.pop(0)
        # 도착지 도착했으면 config 1로 바꾸고 break
        if arr[x][y] == 3:
            config = 1
            break
        # 방문체크
        arr[x][y] = 1
        # delta를 이용해서 이동할 수 있는 지점 찾기
        for i, j in delta:
            new_x = x + i
            new_y = y + j
            if 0 <= new_x <= 15 and 0 <= new_y <= 15 and arr[new_x][new_y] != 1:
                stack.append((new_x, new_y))
    print(f'#{tc} {config}')