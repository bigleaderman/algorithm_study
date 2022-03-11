from sys import stdin

n = int(stdin.readline())
lst = [0] + list(map(int, stdin.readline().split()))
# 가장 큰 값이 들어 갈 경우를 가정하여 10^7으로 우선 value 설정
value = [0] + [10 ** 7] * (n)
# value 값은 그 index의 가장 작은 값이 들어가도록 설정하고 이 후 value를 구할 때도 이전 value를 사용하낟.
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if value[i] > value[i - j] + lst[j]:
            value[i] = value[i - j] + lst[j]
print(value[n])