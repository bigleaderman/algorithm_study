import sys
sys.stdin = open('rotation.txt', 'r')
for tc in range(1, int(input())+1):
    n = int(input())
    print_list = [[''] for _ in range(n)]
    print_list_1 = [[''] for _ in range(n)]
    print_list_2 = [[''] for _ in range(n)]
    word_list = [input().split() for _ in range(n)]
    for j in range(n):
        for i in range(n-1,-1,-1):
            print_list[j] += word_list[i][j]
    for k in range(n-1, -1, -1):
        print_list_1[n-k-1] = word_list[k][::-1]
    for j in range(n-1,-1,-1):
        for i in range(n):
            print_list_2[n-j-1] += word_list[i][j]
    print_list = list(map(''.join,print_list))
    print_list_1 = list(map(''.join,print_list_1))
    print_list_2 = list(map(''.join, print_list_2))
    print(f'#{tc}')
    for a in range(n):
        print(print_list[a], end=' ')
        print(print_list_1[a], end=' ')
        print(print_list_2[a], end=' ')
        print()