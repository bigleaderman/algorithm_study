import sys
sys.stdin = open('벌꿀.txt', 'r')

def dfs(n, cnt, ssum, lst): #n은 lst의 인덱스, cnt는 얼마의 꿀이 들어 있는지, ssum은 꿀의 가격
    global sol
    if cnt > C:
        return
    if n == M:
        if ssum > sol:
            sol = ssum
        return
    dfs(n+1, cnt+lst[n], ssum + lst[n]**2, lst)
    dfs(n+1, cnt, ssum, lst)


for tc in range(1, int(input()) + 1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 0

    # 메모이제이션
    memorization = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N-M+1):
            sol = 0
            dfs(0, 0, 0, arr[i][j:j+M])
            memorization[i][j] = sol

    for i1 in range(N):
        for j1 in range(N-M+1):
            for i2 in range(N):
                s = 0
                if i1 == i2:
                    s = j1+M
                for j2 in range(s, N-M+1):
                    ans = max(ans, memorization[i1][j1] + memorization[i2][j2])
    print(f'#{tc} {ans}')