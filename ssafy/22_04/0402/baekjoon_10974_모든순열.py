def parm(k):
    if k == N:
        print(*p)
    else:
        for i in range(1, N+1):
           if not visited[i - 1]:
                visited[i - 1] = 1
                p[k] = i
                parm(k+1)
                visited[i - 1] = 0
N = int(input())
p = [0] * N
visited = [0] * N
parm(0)