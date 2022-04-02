# 팩토리를 열의 idx로 받오올 예정이다. 결국 factory가 깊이가 된다.
def parm(factory, value): #factory : 열idx, 공장, 깊이. value = 값들의 합
    global min_value
    if value > min_value:
        return
    if factory == N:
        if min_value > value:
            min_value = value
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            parm(factory+1, value + arr[i][factory])
            visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    min_value =  99 * 15
    parm(0, 0)
    print(f'#{tc} {min_value}')