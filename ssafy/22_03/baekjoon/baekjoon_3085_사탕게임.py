from sys import stdin

N = int(input())
arr = [list(stdin.readline().strip()) for _ in range(N)]
max_total = 0
# 전체를 돌면서 교환하기
for i in range(N):
    for j in range(N):
        # 가로 교체
        x, y= 0, 1
        new_i = i + x
        new_j = j + y
        # 범위 내에 있을 경우 겹치는 것을 교체하기
        if 0 <= new_j < N:
            arr[i][j], arr[new_i][new_j] = arr[new_i][new_j], arr[i][j]
            # 가로 교체할 경우에는 교체한 부분에 세로 부분과 그 가로줄만 탐색하면 된다.
            # 교체한 부분의 세로 부분 탐색하기
            for a in range(N):
                for b in [j, new_j]:
                    x1 = 1
                    n = 1
                    total = 1
                    while 0 <= a + x1 * n < N and arr[a][b] == arr[a + x1 * n][b]:
                        total += 1
                        n += 1
                    if max_total < total:
                        max_total = total
            # 교체한 가로 한줄 탐색하기
            a = i
            for b in range(N):
                y1 = 1
                n = 1
                total = 1
                while 0 <= b + y1 * n < N and arr[a][b] == arr[a][b + y1 * n]:
                    total += 1
                    n += 1
                if max_total < total:
                    max_total = total

            arr[i][j], arr[new_i][new_j] = arr[new_i][new_j], arr[i][j]
        x, y = 1, 0
        new_i = i + x
        new_j = j + y
        if 0 <= new_i < N:
            arr[i][j], arr[new_i][new_j] = arr[new_i][new_j], arr[i][j]
            for a in [i, new_i]:
                for b in range(N):
                    y1 = 1
                    n = 1
                    total = 1
                    while 0 <= b + y1 * n < N and arr[a][b] == arr[a][b + y1 * n]:
                        total += 1
                        n += 1
                    if max_total < total:
                        max_total = total
            arr[i][j], arr[new_i][new_j] = arr[new_i][new_j], arr[i][j]
            b = j
            for a in range(N):
                x1 = 1
                n = 1
                total = 1
                while 0 <= a + x1 * n < N and arr[a][b] == arr[a + x1 * n][b]:
                    total += 1
                    n += 1
                if max_total < total:
                    max_total = total
print(max_total)