import sys
sys.stdin = open('요리사.txt', 'r')

from itertools import combinations as combi

for tc in range(1, int(input())+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    arr = list(range(N))
    combination = list(combi(arr, N//2))
    min_dif = 98765432
    for cook in combination[:len(combination)]:
        A = 0
        B = 0
        for i in range(N):
            for j in range(N):
                if i != j:
                    if i in cook and j in cook:
                        A += lst[i][j]
                    elif not i in cook and not j in cook:
                        B += lst[i][j]
        dif = abs(A - B)
        if dif < min_dif:
            min_dif = dif
    print(f'#{tc} {min_dif}')