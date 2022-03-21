# 실패한 이유는 위 그림과 같이 비교할 필요 없는 값들을 계속 비교 해줬기 때문이다.
from sys import stdin
n = int(stdin.readline())
lst = [0]*n
top = list(map(int , stdin.readline().split()))

for i in range(1, n):
    first_top = top[i]
    for j in range(i-1, -1, -1):
        if first_top <= top[j]:
            lst[i] = j + 1
            break
print(*lst)

