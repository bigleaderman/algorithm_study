from sys import stdin
n = int(stdin.readline())
stack = [[n, 0]]    # 얼만큼 지나갔는지 파악하기위해서 value값과 cnt값 두개를 리스트로 stack
visited = [50]*(n+1)    # visited 인덱스에 cnt값이 들어간다. 50을 넣은 이유는 10^6이 50보다 작았기 때문이다.
min_cnt = 1000000   # min_cnt는 10^6 보다 cnt는 작을거 같아서 min_cnt로 넣어줬다.

while stack:    #dp
    num = stack.pop()
    # 가지치기
    # 가장 작은 값을 찾는게 목적이기 때문에 num의 cnt는 무조건 min_cnt보다 작아야한다.
    # 그리고 반복되는 것을 막기 위해서 방문했던것의 cnt가 현재 num cnt보다 클때만 진행
    if num[1] < min_cnt and visited[num[0]] > num[1]:
        # 위 조건을 다 만족하고 num value가 1이기 때문에 min_cnt가 num value 값이다.
        if num[0] == 1:
            min_cnt = num[1]
        # 1을 빼주는 조건이 있기 때문에 1빼고 cnt +1
        stack.append([num[0] - 1, num[1] + 1])
        # 2로 나누어 떨어지거나 3으로 나누어 떨어질 때 stack에 나눈몫과 cnt push
        if not num[0] % 2:
            stack.append([num[0] // 2, num[1] + 1])
        if not num[0] % 3:
            stack.append([num[0] // 3, num[1] + 1])
        # 방문체크(num의 cnt push)
        visited[num[0]] = num[1]
print(min_cnt)