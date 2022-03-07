n = int(input())
square = [list(map(int, input().split())) for _ in range(n)]
area = [[0]*100 for _ in range(100)]
for i in range(n):
    for j in range(square[i][0], square[i][0]+10):
        for k in range(square[i][1], square[i][1]+10):
            area[j][k] = 1
total = 0
for i in range(100):
    total += sum(area[i])
print(total)