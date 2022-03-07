from sys import stdin
num = int(stdin.readline())
my_list = [int(stdin.readline()) for _ in range(num)]
max_num = my_list[-1]
total = 1
for i in my_list[::-1]:
    if i > max_num:
        max_num = i
        total += 1
print(total)