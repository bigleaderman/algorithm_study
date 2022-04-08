from sys import stdin

def dfs(ni,nj):
    global num
    for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nni, nnj = ni + x, nj + y
        if 0 <= nnj < N and 0 <= nni < N and arr[nni][nnj] == '1':
            num += 1
            arr[nni][nnj] = 0
            dfs(nni, nnj)

N = int(stdin.readline().strip())
arr = [list(stdin.readline().strip()) for _ in range(N)]
cnt = 0
numbers = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1':
            arr[i][j] = 0
            cnt += 1
            num = 1
            dfs(i, j)
            numbers.append(num)
numbers.sort()
print(cnt)
for i in numbers:
    print(i)