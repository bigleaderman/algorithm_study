import sys
sys.stdin = open('sample_input (4).txt', 'r')

for tc in range(int(input())):
    word = list(input())
    while True:
        for i in range(len(word) - 1):
            if word[i] == word[i+1]:
                word.pop(i)
                word.pop(i)
                break
        else:
            break
    print(f'#{tc+1} {len(word)}')
