n = int(input())
arr = []
for i in range(n):
  arr.append(input())
set_arr = list(set(arr))
set_arr.sort()
set_arr.sort(key =len)
for i in set_arr:
  print(i)