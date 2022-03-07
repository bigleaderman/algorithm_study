import  sys
sys.stdin = open('sw_1209.txt', 'r')

for _ in range(1, 11):
    tc = int(input())
    row_lst = [list(map(int, input().split())) for _ in range(100)] #row 기준으로 열을 나열 list
    col_lst = list(zip(*row_lst))   #col 기준으로 행을 나열 list
    max_total = 0 # max_total 0으로 초기화
    for i in range(100):
        row_sum = sum(row_lst[i])
        col_sum = sum(col_lst[i])
        cross_left = 0
        cross_right = 0
        cross_left += row_lst[i][i]
        cross_right += row_lst[i][99-i]
        if row_sum >= max_total:
            max_total = row_sum
        if col_sum >= max_total:
            max_total = col_sum
    if cross_left >= max_total:
        max_total = cross_left
    if cross_right >= max_total:
        max_total = cross_right
    print(f'#{tc} {max_total}')

