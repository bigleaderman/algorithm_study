from sys import stdin
# 이문제는 dfs를 풀었는데 예제로는 다 맞았다 하지만 submit 0%에서 멈췄다
# 그리고 bfs와 visited을 활용해서 풀었는데 이거 역시 75%까지는 가다가 틀렸따
# 그리고 bfs 정석으로 풀었을때는 맞았다. 이유를 모르겠다.
def bfs(i, j, c):
    Q = [[i, j, c]]
    front = 0
    rear = 1
    while front != rear:
        ni, nj, cnt = Q[front]
        front += 1
        if (ni, nj) == (N-1, M-1):
            return cnt
        for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nni, nnj = ni + x, nj + y
            if 0 <= nni < N and 0 <= nnj < M and arr[nni][nnj] == '1':
                arr[nni][nnj] = 0
                rear += 1
                Q.append([nni, nnj, cnt + 1])

N, M = map(int, stdin.readline().split())
arr = [list(stdin.readline().strip()) for _ in range(N)]
print(bfs(0, 0, 1))