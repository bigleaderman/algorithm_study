from sys import stdin

N, target = map(int, stdin.readline().split())
dongjeon = [int(stdin.readline()) for _ in range(N)][::-1]
cnt = 0

# 동전을 큰 값 부터 받아오고 나누어 떨어지는 값을 빼줘서 0 이될까지 반복
for money in dongjeon:
    n = target // money
    if n:
        target -= money * n
        cnt += n
print(cnt)