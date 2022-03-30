def f(i, j, v): # 현재위치[i, j], v는 value값
    global min_value

    v += arr[i][j]

    if v > min_value:
        return

    if i == j == N-1:
        min_value = v

    for x, y in [[1, 0], [0, 1]]:
        new_i, new_j = i + x, j +y
        if 0 <= new_i < N and 0 <= new_j < N:
            f(new_i, new_j, v)


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_value = 1690
    f(0, 0, 0)
    print(f'#{tc} {min_value}')