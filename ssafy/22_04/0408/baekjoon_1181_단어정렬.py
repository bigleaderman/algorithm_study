N = int(input())
max_length = 0
length = 1
words = []
ans = []
for _ in range(N):
    word = input()
    max_length = max(max_length, len(word))
    words.append(word)
words.sort()
while length != max_length+1:
    for i in range(len(words)):
        if len(words[i]) == length:
            if words[i] not in ans:
                ans.append(words[i])
    length += 1
for a in ans:
    print(a)