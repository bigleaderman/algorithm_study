E, S, M = map(int, input().split())
for i in range(100000):
    E1, S1, M1 = i % 15 + 1, i % 28 + 1, i % 19 + 1
    if [E1, S1, M1] == [E, S, M]:
        print(i+1)
        break
