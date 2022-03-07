import sys
sys.stdin = open('sample_input (1).txt','r')
for tc in range(int(input())): # test case 마다 받아오기
    n, l = map(int, input().split()) # node와 line 받기
    num_list = [[] for _ in range(n+1)] #인덱스 별로 도착지를 받기 위한 list 만들기
    count_list = [] # 숫자를 파악 할 list 만들기
    for _ in range(l): # 인덱스 안에 value 값들 넣어서 어디 인덱스에서 출발 할 경우에 어떤 value까지 도착할 수 있는지 확인.
        i, v = map(int, input().split())
        num_list[i].append(v)
    for i in range(len(num_list)): #현재 index안에 있는 len를 파악하기
        count_list.append(len(num_list[i]))
    s, e = map(int, input().split())
    stack = [s]
    result = 0
    while stack:
        if s == e:
            result = 1
            break
        elif num_list[s]:
            stack.append(num_list[s][0])
            count_list[s] -= 1
            s = num_list[s].pop(0)
        elif count_list[s] == 0:
            s = stack.pop()
    print(f'#{tc+1} {result}')




