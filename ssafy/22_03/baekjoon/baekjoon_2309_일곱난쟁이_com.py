from itertools import combinations

# 조합을 이용
nanjaengs = [int(input()) for _ in range(9)]
nanjaengs.sort()
for nanjaeng_7 in list(combinations(nanjaengs, 7)):
    if sum(nanjaeng_7) == 100:
        for person in nanjaeng_7:
            print(person)
        break
