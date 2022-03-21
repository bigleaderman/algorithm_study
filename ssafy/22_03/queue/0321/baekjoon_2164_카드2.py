from sys import stdin

N = int(stdin.readline())
# front는 idx 젤 앞인 0 rear은 값이 들어갈 수 있는 idx인 N을 준다.
front = 0
rear = N
# append, pop을 이용하고 싶지 않아서 list를 미리 만든다. 반씩 줄어들기 때문에 N만큼 미리 채우면
# out of range 문제가 없어짐
Q = list(range(1, N + 1)) + [0] * N
# rear과 front를 이용하여 append, pop을 사용
while rear - front != 1:
    front += 1
    Q[rear] = Q[front]
    front += 1
    rear += 1
print(Q[front])