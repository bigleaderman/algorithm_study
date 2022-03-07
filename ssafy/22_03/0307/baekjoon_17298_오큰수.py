from sys import stdin

n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
#for문에 첫 값을 안 넣기 위해서 stack에 lst[-1]미리 넣었고,
# 문제에서 가정에 벗어날 경우 -1을 출력해야 하기 때문에 answer list에 -1을 default 값으로 넣기
stack, answer = [lst[-1]], [-1]*n

# 전체 값은 꼭 확인을 해야 하므로 이 반복문을 넣었다.
for i in range(-2, -n-1, -1):
    #stack에 있을 경우에는 계속 반복한다.
    while stack:
        # lst[i] 값이 stack[-1] 값보다 작을 경우 stack value가 lst value 보다 크고
        # 오른쪽에 있는 수중에 가장 왼쪽인 수므로 asnwer에 현위치 인덱스 값에 stack[-1] 넣기
        if lst[i] < stack[-1]:
            answer[i] = stack[-1]
            break
        # 위 가정이 틀렷을 경우 stack에서 이 값들 필요없는 값이므로 pop을 해준다.
        else:
            stack.pop()
    # 현재 값은 다음 값의 오른쪽에 있으면서 가장 왼쪽에 있는 값이므로 push해준다.
    stack.append(lst[i])
print(*answer)