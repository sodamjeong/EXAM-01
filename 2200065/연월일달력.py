 # 2056. 연월일달력
 # 
 # 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다.
 # 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 ”YYYY/MM/DD”형식으로 출력하고,
 # 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라. 

t = int(input())
day = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31 }

for i in range(1, t + 1):
    n = input()
    a = n[:4]
    b = n[4:6]
    c = n[6:]
    if int(b) not in day:
        print(f'#{i}',-1)
    else:
        if int(c) > day[int(b)] or int(c) <= 0:
            print(f'#{i}',-1)
        else:
            print(f'#{i}',a+'/'+b+'/'+c)     

