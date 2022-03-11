from sys import stdin

# sw문제 보다 쉬운 문제 조건식 아주 쉽게 찾음
n = int(stdin.readline())
lst = [1, 2]
if n != 1 and n != 2:
    for i in range(2, n):
        lst.append(lst[i - 1] + lst[i - 2])
print(lst[n-1] % 10007)