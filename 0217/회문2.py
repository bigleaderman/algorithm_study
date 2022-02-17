import sys
sys.stdin = open('input.txt', 'r')


def solve(N, M, word_list, new_word_list):
    for _ in range(100):
        for a in range(N):
            for b in range(N-M+1):
                palindrome = word_list[a][b:M+b]
                palindrome_N = new_word_list[a][b:M + b]
                if palindrome[:M//2] == palindrome[::-1][:M//2]:
                    return len(palindrome)
                elif palindrome_N[:M//2] == palindrome_N[::-1][:M//2]:
                    return len(palindrome_N)
        M -= 1

for _ in range(10):
    tc = input()
    N, M = 100, 100
    word_list = [list(input()) for _ in range(N)]
    #전치행렬 만들기
    new_word_list = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            new_word_list[j][i] = word_list [i][j]
    print(f'#{tc} {solve(N, M, word_list, new_word_list)}')