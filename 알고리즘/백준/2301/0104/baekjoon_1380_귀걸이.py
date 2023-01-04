from sys import stdin

answer = []
now = 0

while True:
    now += 1
    number = int(stdin.readline())
    if number:
        person_name = []
        conf = [0] * number
        for _ in range(number):
            name = stdin.readline()
            person_name.append(name)
        for _ in range(number):
            N, S = stdin.readline().split()
        for _ in range(number-2):
            N, S = stdin.readline().split()
            conf[int(N) - 1] = 1
        answer.append(person_name)
    else:
        break