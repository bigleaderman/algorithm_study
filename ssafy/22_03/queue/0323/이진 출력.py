N = list(map(int, input()))
asw = []
for i in range(0, 70, 7):
    n = N[i]
    for j in range(i + 1, i + 7):
        n = n * 2 + N[j]
    asw.append(n)
print(*asw, sep=', ')