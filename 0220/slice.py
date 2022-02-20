import sys
sys.stdin = open('slice.txt', 'r')

# for tc in range(int(input())):
#     batch = input()
#     slicing = []
#     steel = []
#     total = 0
#     for i in range(len(batch)):
#         if batch[i:i+2] == '()':
#             for j in range(len(steel)):
#                 steel[j] = steel[j] + 1
#         elif batch[i-1: i+1] == '()':
#             pass
#         elif batch[i] == '(':
#             steel.append(1)
#         elif batch[i] == ')':
#             total += steel.pop()
#     print(f'#{tc+1} {total}')

for tc in range(1, int(input()) + 1):
    steel = input().replace('()', '.')
    stack, answer = [], 0
    for i in steel:
        if i == '.':
            answer += len(stack)
        elif i == ')':
            answer += stack.pop()
        else:
            stack.append(1)
    print(f'#{tc} {answer}')