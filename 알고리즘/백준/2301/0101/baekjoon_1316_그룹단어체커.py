from sys import stdin

num = int(stdin.readline())
answer = 0

for _ in range(num):
    word = stdin.readline().strip()
    word_dict = {}
    before_word = word[0]
    conf = 1
    for w in word:
        if w in word_dict and before_word != w:
            conf = 0
            break
        elif w in word_dict:
            pass
        else:
            word_dict[w] = 1
        before_word = w
    if conf:
        answer += 1

print(answer)