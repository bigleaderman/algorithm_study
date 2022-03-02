a = int(input())    #switch의 크기
num_list = list(map(int,input().split()))   #switch 현 상태
n = int(input())    #스위치 조정할 사람 숫자

for _ in range(n):  #사람 수만큼 조정을 반복
    gender, num = map(int, input().split())

    if gender == 1: #남자일때
        i = 1   #배수를 해주기 위해 i를 1로 설정
        while num * i <= a: #switch크기 안에 있을 경우
            if num_list[num*i-1]:
                num_list[num*i-1] = 0
            else:
                num_list[num*i-1] = 1
            i += 1  #배수 처리를 해주기 위하여 i를 1씩 증가시키기

    elif gender == 2:   #여자 일 때
        i = 0   #좌우를 확인 하기 위하여 i를 0 으로 지정
        while 0 <= num-1-i and num+i <= a and num_list[num-1-i] == num_list[num-1+i]:   #양 옆이 범위 안에 있고 양 옆이 같은때
            if num_list[num-1-i]:   #양쪽 옆을 모두 바꿔주는 코드
                num_list[num-1-i], num_list[num-1+i] = 0, 0
            else:
                num_list[num-1-i], num_list[num-1+i] = 1, 1
            i += 1

for i in range(0, len(num_list), 20):
    print(*num_list[i:i+20])