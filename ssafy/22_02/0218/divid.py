import sys
sys.stdin = open('divid.txt', 'r')

for tc in range(int(input())):
    num = int(input())
    num_list = [2, 3, 5, 7, 11]
    idx = -1
    for i in num_list:
        div = i
        idx += 1
        num_list[idx] = 0
        while num % div == 0:
            num = num // div 
            num_list[idx] += 1
    print(f'#{tc+1}', *num_list)