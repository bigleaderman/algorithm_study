from sys import stdin

n = int(stdin.readline())
# index랑 카드의 수랑 맞춰주기 위해서 [0] + list
lst = [0] + list(map(int, stdin.readline().split()))
value = [0] * (n + 1)
# value의 index에는 그 수의 카드를 구할 때 가장 큰 수만 들어갈 수 있도록 설정 다음 카드를 더 할 때도 사용
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if value[i] < value[i - j] + lst[j]:
            value[i] = value[i - j] + lst[j]
print(value[n])