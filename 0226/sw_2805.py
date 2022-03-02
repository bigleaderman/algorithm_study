import sys
sys.stdin = open('farm.txt', 'r')

for tc in range(1, int(input())+1):
    n = int(input())
    n_list = [list(map(int,input())) for _ in range(n)]
    total = 0
    for i in range(n):
        if i <= n//2:
            total += sum(n_list[i][n//2 - i : n//2 + i + 1])
        else:
            total += sum(n_list[i][i - n//2 : n//2*3 - i + 1])
    print(f'#{tc} {total}')