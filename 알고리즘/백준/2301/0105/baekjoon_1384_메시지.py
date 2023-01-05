from sys import stdin

group = 1
while True:
    number = int(stdin.readline())
    if number == 0:
        break
    name = []
    answer = []
    for i in range(number):
        now = list(stdin.readline().split())
        name.append(now[0])
        for j in range(1, number):
            if now[j] == 'N':
                answer.append([i, i-j])
    print("Group", group)
    if not answer:
        print("Nobody was nasty")
        print()
    else:
        for i, j in answer:
            print(name[j], "was nasty about", name[i])
        print()

    group += 1