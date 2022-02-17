import sys
sys.stdin = open('palindrome.txt', 'r')

for tc in range(int(input())):
    N, M = map(int, input().split())
    word_list = [list(input()) for _ in range(N)]
    #전치행렬 만들기
    new_word_list = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_word_list[j][i] = word_list [i][j]
    for a in range(N):
        for b in range(N-M+1):
            palindrome = word_list[a][b:M+b]
            palindrome_N = new_word_list[a][b:M + b]
            if palindrome[:M//2] == palindrome[::-1][:M//2]:
                word = ''.join(palindrome)
                print(f'#{tc+1} {word}')
            elif palindrome_N[:M//2] == palindrome_N[::-1][:M//2]:
                word = ''.join(palindrome_N)
                print(f'#{tc+1} {word}')