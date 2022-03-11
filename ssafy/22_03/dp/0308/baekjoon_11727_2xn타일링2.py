from sys import stdin

# sw문제와 동일한 문제
# 이번에는 조건식을 찾았는데 빨리 찾는 방법을 모르겠다.
n = int(stdin.readline())
lst = [1, 3] + [0] * (n-2)
if n != 1 and n != 2:
    for i in range(2, n):
        lst[i] = lst[i - 1] + 2 * lst[i - 2]
print(lst[n - 1] % 10007)