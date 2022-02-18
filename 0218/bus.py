import sys
sys.stdin = open('bus.txt', 'r')

for tc in range(int(input())):
    n = int(input())
    num_list = list(map(int, input().split()))[::-1]
    max_num = num_list[0]
    total = 0
    for i in num_list:
        if max_num > i:
            total += (max_num - i)
        else:
            max_num = i
    print(f'#{tc+1} {total}')
