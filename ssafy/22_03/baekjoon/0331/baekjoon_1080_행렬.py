from sys import stdin
# 완전 검색을 이용
N, M = map(int, stdin.readline().split())
arr1 = [list(map(int, stdin.readline().strip())) for _ in range(N)]
arr2 = [list(map(int, stdin.readline().strip())) for _ in range(N)]
cnt = 0
# 다른 값들 찾기
for i in range(N-2):
    for j in range(M-2):
        if arr1[i][j] != arr2[i][j]:
            cnt += 1
            for a in range(3):
                for b in range(3):
                    if arr1[i+a][j+b]:
                        arr1[i+a][j+b] = 0
                    else:
                        arr1[i+a][j+b] = 1

config = 1
for i in range(N):
    if config:
        for j in range(M):
            if arr1[i][j] != arr2[i][j]:
                config = 0
                break

if config:
    print(cnt)
else:
    print(-1)
