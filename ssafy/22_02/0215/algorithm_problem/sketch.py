import sys
sys.stdin = open('sample_input (4).txt', 'r')

for tc in range(int(input())):
    total = 0
    sketch_list = [[0]*10 for _ in range(10)]
    for _ in range(int(input())):
        num = list(map(int, input().split()))
        for i in range(num[0], num[2]+1):
            for j in range(num[1], num[3]+1):
                sketch_list[i][j] += num[4]
    for a in range(10):
        for b in range(10):
            if sketch_list[a][b] == 3:
                total += 1
    print(f'#{tc+1} {total}')
