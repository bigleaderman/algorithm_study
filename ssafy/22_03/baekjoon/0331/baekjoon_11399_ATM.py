from sys import stdin
# 그냥 정렬
N = int(stdin.readline())
numbers = list(map(int, input().split()))
numbers.sort()
total = 0
for i in range(N):
    total += sum(numbers[:i+1])
print(total)