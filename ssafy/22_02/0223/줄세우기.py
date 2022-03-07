num = int(input())
student_list = [i for i in range(1,num+1)]
ticket = list(map(int, input().split()))
for j in range(1, len(ticket)):
    student_list  = student_list[0:j-ticket[j]] + student_list[j:j+1] + student_list[j-ticket[j]:]
    student_list.pop(j+1)
print(*student_list)

