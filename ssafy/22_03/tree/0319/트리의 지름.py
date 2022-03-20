from sys import stdin

N = int(stdin.readline())
tree = [[0] * 3 for _ in range(N+1)]
max_value = 0
# idx 0, 1은 자식들 2는 부모 3은 1을 제외한 자신의 value값
for _ in range(N-1):
    p, c, v = map(int, stdin.readline().split())
    if tree[p][0] == 0:
        tree[p][0] = [c, v]
    else:
        tree[p][1] = [c, v]
    tree[c][2] = [p, v]

# 이동의 시작점은 젤 끝 부터 자식이 생기기 전까지
for i in range(N, 0, -1):
    # 자식이 생기면 break
    if tree[i][0] != 0 or tree[i][0] != 0:
        continue
    Q = [[i, 0]]
    visited = [0] * (N+1)
    while Q:
        now = Q.pop(0)
        visited[now[0]] = 1
        # 만약 자식이 없다면 끝으로 도착한 것이기 때문에 최대값과 비교
        if now[1] > max_value:
            max_value = now[1]
        # 안에 있는 value들을 3개로 돌아가면서 찾기
        for j in range(3):
            if tree[now[0]][j]:
                go = tree[now[0]][j][0]
                if i > go and not visited[go]:
                    Q.append([go, now[1] + tree[now[0]][j][1]])
print(max_value)
