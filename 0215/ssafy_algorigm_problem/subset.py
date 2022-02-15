import sys
sys.stdin = open('sample_input (3).txt', 'r')

def subset(N ,K):
    num_list = list(i for i in range(1,13))
    n = len(num_list)
    total = 0
    for i in range(1<<n):
        number, sum = 0, 0
        for j in range(n):
            if i & (1<<j):
                sum += num_list[j]
                number += 1
        if number == N and sum == K:
            total += 1
    return total

for tc in range(int(input())):
    N, K = map(int, input().split())
    print(f'#{tc+1} {subset(N, K)}')