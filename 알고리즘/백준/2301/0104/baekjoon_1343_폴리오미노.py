from sys import stdin

word = stdin.readline().strip().replace("XXXX", "AAAA").replace("XX", "BB")
if "X" in word:
    print(-1)
else:
    print(word)