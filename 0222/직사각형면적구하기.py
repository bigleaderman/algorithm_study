square = [list(map(int, input().split())) for _ in range(4)]
area_list = [[0]*100 for _ in range(100)]
for i in range(4):
    for j in range(square[i][0], square[i][2]):
        for k in range(square[i][1], square[i][3]):
            area_list[j][k] = 1
total = 0
for k in range(100):
    total += sum(area_list[k][:100])
print(total)
