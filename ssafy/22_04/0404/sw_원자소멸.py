di = (1, -1, 0, 0)
dj = (0, 0, -1, 1)
for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    asw = 0
    for i in range(len(arr)):
        arr[i][0], arr[i][1] = arr[i][0] * 2, arr[i][1] * 2

    for _ in range(4002):

        for i in range(len(arr)):
            arr[i][0], arr[i][1] = arr[i][0] + dj[arr[i][2]], arr[i][1] + di[arr[i][2]]

        ddel, v = set(), set()
        for i in range(len(arr)):
            if (arr[i][0], arr[i][1]) in v:
                ddel.add((arr[i][0], arr[i][1]))
            v.add((arr[i][0], arr[i][1]))

        for i in range(len(arr)-1, -1, -1):
            if (arr[i][0], arr[i][1]) in ddel:
                asw += arr[i][3]
                arr.pop(i)
    print(f'#{tc} {asw}')