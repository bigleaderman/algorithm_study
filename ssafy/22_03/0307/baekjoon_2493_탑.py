from sys import stdin

n = int(stdin.readline())
#value값과 인덱스 값을 받아온다. 이것을 통해서 asnwer에 값을 넣는다
lst = [[idx, value] for idx, value in enumerate(list(map(int, stdin.readline().split())),start=1)]
answer, stack = [0]*n, [lst[0]]

#전체 반복문을 돌면서 값을 확인
for i in range(1,n):
    # stack이 있을 때 까지 반복한다.
    while stack:
        # 현재 lst의 value 값이 stack의 value 값 보다 작을 경우에 송신이 갔으니 answer에 stack idx값을 넣어준다.
        if lst[i][1] <= stack[-1][1]:
            answer[i] = stack[-1][0]
            break
        # 만약 위 가정이 아니라면 그 다음 idx의 value를 비교할때 stack[-1] value보다 현재 value가
        # 크기 때문에 이 값은 pop을 해서 시간을 줄여준다.
        else:
            stack.pop()
    # 현재의 value값은 가장 오른쪽에 있고 다음의 value값보다 클 수 있기 때문에 push 해준다.
    stack.append(lst[i])
print(*answer)