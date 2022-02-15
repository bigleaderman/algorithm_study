import sys
sys.stdin = open('input (4).txt','r')
for tc in range(int(input())):
    num = int(input())
    num_list = list(map(int, input().split()))
    idx = 0
    while True:
        if idx == 10:
            break
        max_idx = idx
        min_idx = idx
        for i in range(idx, num):
            if num_list[i] > num_list[max_idx]:
                max_idx = i
        num_list[idx], num_list[max_idx] = num_list[max_idx], num_list[idx]
        for i in range(idx, num):
            if num_list[i] < num_list[min_idx]:
                min_idx = i
        num_list[idx+1], num_list[min_idx] = num_list[min_idx], num_list[idx+1]
        idx += 2
    print(f'#{tc+1}', end=' ')
    print(*num_list[:10])