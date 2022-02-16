import sys
sys.stdin = open('input (5).txt','r')

for tc in range(int(input())):
    M, N = map(int, input().split())
    num_list = [list(map(int, input().split())) for _ in range(M)]
    max_num = 0
    for i in range(M- N + 1):
        for j in range(M - N + 1):
            total = 0
            for a in range(N):
                for b in range(N):
                    total += num_list[i+a][j+b]
            if total > max_num:
                max_num = total
    print(f'#{tc+1} {max_num}')