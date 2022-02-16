import sys
sys.stdin = open('input1.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(N)]
    max_total = 0
    for i in range(N):
        total = 0
        for j in range(M):
            if num_list[i][j]:
                total += 1
                if total > max_total:
                    max_total = total
            else:
                total = 0
    for j in range(M):
        total = 0
        for i in range(N):
            if num_list[i][j]:
                total += 1
                if total > max_total:
                    max_total = total
        else:
            total = 0
    print(f'#{tc+1} {max_total}')