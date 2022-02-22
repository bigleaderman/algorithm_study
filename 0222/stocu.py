import sys
sys.stdin = open('stocu.txt', 'r')

for tc in range(1, int(input()) + 1):
    num_list = [list(map(int, input().split())) for _ in range(9)]
    result = 1
    delta = [(0,0), (1,0), (1,1), (1,-1), (0,1), (0,-1), (-1,-1), (-1,0), (-1,1)]
    for i in range(9):
        check_row = 45
        check_col = 45
        for j in range(9):
            if i % 3 == 1 and j % 3 == 1:
                check_9 = 45
                for k in range(9):
                    check_9 -= num_list[i+delta[k][0]][j+delta[k][1]]
                if check_9 != 0:
                    result = 0
                    break
            check_row -= num_list[i][j]
            check_col -= num_list[j][i]
        if check_col != 0 or check_row != 0:
            result = 0
            break
    print(f'#{tc} {result}')