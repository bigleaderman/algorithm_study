from sys import stdin

word = list(stdin.readline().strip())
answer_list = []

for i in range(0, len(word)-2):
    for j in range(i+1, len(word)-1):
        first = word[0:i+1]
        second = word[i+1:j+1]
        third = word[j+1:]

        first.reverse()
        second.reverse()
        third.reverse()

        answer_list.append(''.join(first+second+third))

answer_list.sort()
print(answer_list[0])