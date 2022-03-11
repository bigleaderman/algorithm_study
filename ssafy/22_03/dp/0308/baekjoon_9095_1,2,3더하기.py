from sys import stdin

# input을 제대로 읽자 반복문 안돌려서 틀렸다.
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    stack = [n]
    cnt = 0
    # dp를 하면서 num이 0이 될때 마다 cnt + 1
    # dp를 돌면서 모든 계산식이 순서대로 들어가기 때문에 방문 조건을 안주고 돌기만 하면된다.
    while stack:
        num = stack.pop()
        if not num:
            cnt += 1
            continue
        if num >= 3:
            stack.append(num-3)
        if num >= 2:
            stack.append(num-2)
        stack.append(num-1)
    print(cnt)