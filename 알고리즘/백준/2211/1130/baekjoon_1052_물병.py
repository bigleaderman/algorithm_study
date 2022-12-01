from sys import stdin

N ,K = map(int, stdin.readline().split())
count = 0
num_list = []
while N > 0 and K > count:
    num = 0
    now = N
    while now // 2 > 0:
        now = now//2
        num += 1
    N -= 2 ** num
    num_list.append(2 ** num)
    count += 1
    # print(2 ** num)
if N:
    print(num_list[-1] * 2 - num_list[-1] - N)
else:
    print(0)
# print(num_list)
# print(N)