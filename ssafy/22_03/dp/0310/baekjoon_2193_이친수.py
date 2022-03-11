# from sys import stdin
# ### Test case는 맞지만 정답 틀림.... 접근법이 틀린듯
# N = int(input())
# pri_lst = [0] + list(map(int,input().split())) #인덱스 맞추기 #뭉티기로 살때가격
# max_lst = [pri_lst[0]] + [pri_lst[1]] # 카드 갯수당 가장 큰 가격
#
# stand = 1  # 현재까지 단위당 카드 수가 가장 비싼 카드팩의 위치를 변수 stand로 정함
# for i in range(2,N+1):
#     now_max = 0
#     if (max_lst[stand] + max_lst[i-stand]) < pri_lst[i]: #현재 카드값(현재 카드 갯수를 뭉티기로사는게) 가격이 더 크다면 stand 교체
#            stand = i
#            now_max = pri_lst[i]
#     else:
#         now_max = max_lst[stand] + max_lst[i-stand] #아니면 가장 큰 뭉티기로 먼저 사고 나머지는 max_lst[i-3]의 가격으로 사기
#     max_lst.append(now_max)
# print(max_lst[-1])
#
# from sys import stdin
#
# n = int(stdin.readline())
# # index랑 카드의 수랑 맞춰주기 위해서 [0] + list
# lst = [0] + list(map(int, stdin.readline().split()))
# value = [0] * (n + 1)
# lst1 = [0]*(n+1)
# # value의 index에는 그 수의 카드를 구할 때 가장 큰 수만 들어갈 수 있도록 설정 다음 카드를 더 할 때도 사용
# for i in range(1, n + 1):
#     for j in range(1, i + 1):
#         if value[i] < value[i - j] + lst[j]:
#             value[i] = value[i - j] + lst[j]
#             lst1[i] = [value[i-j], lst[j]]
# print(lst1)

import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

d = [0] * (n+1)
d[1] = data[0]
for i in range(2,n+1):
    d[i] = data[i-1]
    for j in range(1,i//2+1):
        d[i] = max(d[i], d[i-j]+data[j-1])


print(d[n])