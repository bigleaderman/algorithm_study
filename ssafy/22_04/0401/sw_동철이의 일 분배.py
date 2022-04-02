import sys
sys.stdin = open('동철이.txt','r')

def parm(person, value):
    global max_value
    if person != 0:
        if value <= max_value:
            return
    if person == N:
        max_value = value
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                parm(person + 1, value*arr[i][person])
                visited[i] = 0

for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr[i][j] = arr[i][j]/100
    visited = [0] * N
    max_value = 0
    parm(0, 1)
    max_value = max_value * 100
    print("#{} {:.6f}".format(tc, max_value))