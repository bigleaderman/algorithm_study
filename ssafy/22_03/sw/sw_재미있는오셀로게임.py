for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    lst = [[0] * N for _ in range(N)]
    # 흑돌 백돌 미리 넣기
    lst[N // 2 - 1][N // 2], lst[N // 2][N // 2 - 1] = 1, 1
    lst[N // 2 - 1][N // 2 - 1], lst[N // 2][N // 2] = 2, 2
    blacks = []
    whites = []
    for _ in range(M):
        j, i, value = map(int, input().split())
        # 흑돌과 백돌 구분해서 각 리스트에 넣기
        if value == 1:
            for black_idx in range(len(blacks)):
                # 같은 행에 있는 블랙 돌 찾기
                if blacks[black_idx][0] == i:
                    # 화이트 돌면서 같은 화이트 행 찾기
                    for white_idx in range(len(whites)):
                        if whites[white_idx][0] == i:
                            # 돌의 열을 비교후 사이에 백돌이 사이에 있는지 확인
                            if j > blacks[black_idx][1]:
                                if blacks[black_idx][1] < whites[white_idx][1] < j:
                                    lst[whites[white_idx][0]][whites[white_idx][1]] = 1
                                    blacks.append(whites.pop(white_idx))
                            else:
                                if j < whites[white_idx][1] < blacks[black_idx][1]:
                                    lst[whites[white_idx][0]][whites[white_idx][1]] = 1
                                    blacks.append(whites.pop(white_idx))


            blacks.append([i, j])
        else:
            whites.append([i, j])


        # j 기준으로 찾기
        # 대각선 기준으로 중간 찾기

        lst[y][x] = value
        f