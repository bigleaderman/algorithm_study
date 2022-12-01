from sys import stdin

for _ in range(int(stdin.readline().strip())):
    N, M = map(int, stdin.readline().split())
    N_sum = 1
    M_sum = 1
    for i in range(N, 1, -1):
        N_sum *= i
    for j in range(M, M-N, -1):
        M_sum *= j
    print(M_sum//N_sum)