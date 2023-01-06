from sys import stdin

number = int(stdin.readline())
persons = []

for i in range(number):
    persons.append([int(stdin.readline()), i])


persons.sort(reverse=True)
count = 0
while persons[0][1] != 0:
    persons[0][0] -= 1
    for i in range(1, number):
        if persons[i][1] == 0:
            persons[i][0] += 1
            break
    count += 1
    persons.sort(reverse=True)

print(count)