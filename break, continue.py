#while - break

i = 0
while True:      # 무한루프
    print(i)
    i += 1       # i값 1씩 증가

    if i == 10:  # i가 10일 때
        break   # 반복문을 끝냄, while 제어흐름을 벗어남.  

#for - break

for i in range(10000): # 0 ~ 9999까지 반복
    print(i)

    if i == 10:        # i가 10일 때
        break          # 반복문을 끝냄, for 제어흐름을 벗어남


#for - continue

for i in range(100): # 0부터 99까지 증가하면서 100번 반복
    if i % 2 == 0:   # i를 2로 나누었을 때 나머지가 0면 짝수
        continue     # 아래 코드를 실행하지 않고 건너뜀
    print(i)

#while - continue

i = 0
while i < 100 :
    i += 1
    if i % 2 ==0:
        continue
    print(i)

#for,while with pass

for i in range(10):#10번 반복
    pass           #아무일도 하지 않음

while True:        #10번 반복
    pass           #아무일도 하지 않음
