from sys import stdin

# stack을 이용한 dfs로 근처에 방문되는 섬은 다 0 으로 만들기
# 그럼 떨어져있는 섬만 1이 남게 된다.
# 그래서 전체 순회하면서 dfs가 끝나고도 또 찾으면 cnt + 1 해줘서 cnt를 구하면 섬의 갯수 파악 완료
while True:
    M, N = map(int, stdin.readline().split())
    if not M + N:
        break
    arr = [list(map(int, stdin.readline().split())) for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                cnt += 1
                arr[i][j] = 0
                stack = [[i, j]]
                while stack:
                    ni, nj = stack.pop()
                    for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                        ni1, nj1 = x + ni, y + nj
                        if 0 <= ni1 < N and 0 <= nj1 < M and arr[ni1][nj1]:
                            arr[ni1][nj1] = 0
                            stack.append([ni1, nj1])
    print(cnt)