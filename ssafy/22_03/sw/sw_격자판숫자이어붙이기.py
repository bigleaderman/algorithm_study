delta = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def dfs(num, i, j, last):
    if last == 7:
        asw.add(num)
        return
    for x, y in delta:
        new_i = i + x
        new_j = j + y
        if 0 <= new_i < 4 and 0 <= new_j < 4:
            dfs(num * 10 + arr[new_i][new_j], new_i, new_j, last + 1)

for tc in range(1, int(input()) + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    asw = set()
    last = 1
    for i in range(4):
        for j in range(4):
            dfs(arr[i][j], i, j, last)
    print(f'#{tc} {len(asw)}')