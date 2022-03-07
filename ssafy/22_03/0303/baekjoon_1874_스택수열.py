from sys import stdin

stack = []  # sample input 받아오는 lst
check = []  # 잠시 쌓아두는 list
arr = []    # stack리스트와 같게 만들려는 리스트
plus_minus = []    #append,pop 넣는 리스트
num = int(input())
n = 0
for _ in range(num):
    stack.append(int(stdin.readline()))
for i in range(1, num+1):
    check.append(i)
    plus_minus.append('+')
    while check and check[-1] == stack[n]:
        arr.append(check.pop())
        plus_minus.append('-')
        n += 1
if stack == arr:
    for i in plus_minus:
        print(i)
else:
    print('NO')



