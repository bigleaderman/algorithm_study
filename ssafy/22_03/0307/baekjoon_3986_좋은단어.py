from sys import stdin

total = 0 #좋은 단어 수
for i in range(int(stdin.readline())):
    lst = []
    word = stdin.readline().strip()
    # 홀수는 좋은 단어가 될 수 없으므로 pass
    if len(word) % 2:
        continue
    # word에 value 값을 돌면서 lst는 빈리스트가 되야한다.
    for w in word:
        if lst and w == lst[-1]:
            lst.pop()
        else:
            lst.append(w)
    # 빈 리스트일 경우에는 좋은 단어이다.
    if not lst:
        total += 1
print(total)