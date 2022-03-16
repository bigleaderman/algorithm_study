# 순열 구하기
def f(k):
    if k == 3:
        stack.append([A[N[i]] for i in range(3)])
    for i in range(k, 3):
        N[i], N[k] = N[k], N[i]
        f(k+1)
        N[i], N[k] = N[k], N[i]

# stack에 리스트 순서대로 gate idx 순서 순열이 들어가있다.
A = [0, 1, 2]
N = [i for i in range(3)]
stack = []
f(0)

for tc in range(1, int(input()) + 1):
    people = int(input())
    gate = [list(map(int, input().split())) for _ in range(3)]
    # 실제 게이트 숫자를 받아 오기 위하여 [1]을 앞에 더하기
    visited = [1] + [0] * people
    # 게이트 순열을 돌아가면서 반복하기
    min_num = 99999
    for i in range(len(stack)):
        # 현재 순열의 게이트수를 받아오기
        cnt_1 = 0
        cnt_2 = 0
        for now_gate in stack[i]:

            # 현재 통로의 사람 숫자가 0이 될 때 까지 빼가면서 하기.
            now_1 = 0
            while gate[now_gate][1]:
                if not visited[gate[now_gate][0] + now_1]:
                    visited[gate[now_gate][0] + now_1] = 1
                    gate[now_gate][1] -= 1
                    cnt_1 += now_1 + 1
                if not gate[now_gate][1]:
                    break
                if not visited[gate[now_gate][0] - now_1]:
                    visited[gate[now_gate][0] - now_1] = 1
                    gate[now_gate][1] -= 1
                    cnt_1 += now_1 + 1
            now_2 = 0
            while gate[now_gate][1]:
                if not visited[gate[now_gate][0] + now_2]:
                    visited[gate[now_gate][0] + now_2] = 1
                    gate[now_gate][1] -= 1
                    cnt_2 += now_2 + 1
                if not gate[now_gate][1]:
                    break
                if not visited[gate[now_gate][0] - now_2]:
                    visited[gate[now_gate][0] - now_2] = 1
                    gate[now_gate][1] -= 1
                    cnt_2 += now_2 + 1

