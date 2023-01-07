from sys import stdin

number_list = list(stdin.readline().strip())
number_list.sort(reverse=True)
for num in number_list:
    print(num, end="")