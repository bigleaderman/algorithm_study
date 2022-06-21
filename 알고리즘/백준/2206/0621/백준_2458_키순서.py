from sys import stdin

# 입력값 받기
N, M = map(int, stdin.readline().split())

# 키의 대소를 비교해주는 array
array = [[0] * (N+1) for _ in range(N+1)]

# 입력값을 통해서 array에 비교했던 것을 넣기
for _ in range(M):
    s, t = map(int, stdin.readline().split())
    array[s][t] = 1

# 플로이드 와샬 사용 정점과 정점사이 중간 정점을 통해서 모든 정점에서 다른 모든 정점의 최단거리 구하기
for k in range(1, N+1):
    for i in range(1, N+1):
        if k == i:
            continue
        for j in range(1, N+1):
            if i == j:
                continue
            if array[i][k] and array[k][j]:
                array[i][j] = 1
answer = 0

# 자신의 위치를 기준으로 자신보다 큰 사람, 작은 사람이 다 있으면 자신이 몇번 째 인지 판단가능
for i in range(1, N+1):
    num = 0
    for j in range(1, N+1):
        num += array[i][j] + array[j][i]
    if num == N-1:
        answer += 1
print(answer)
