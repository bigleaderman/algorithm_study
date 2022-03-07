import sys
sys.stdin = open('sw_1220.txt', 'r')

for tc in range(1, 11):
    n = int(input())
    num_lst = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0
    for j in range(n):
        flag = 0
        for i in range(n):
            if num_lst[i][j] == 1:
                flag = 1
            if num_lst[i][j] == 2 and flag:
                cnt += 1
                flag = 0
    print(f'#{tc} {cnt}')