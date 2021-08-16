#while
i = 0 #초기식  
while i < 100: #while 조건식
    print('Hello, World') # 반복할 코드
    i += 1 #변화식

#while 초기값을 감소시키는 예
i = 100
while i > 0 :
    print('Hello, Python', i)
    i -= 1
    
#초기값을 횟수대로 반복하기

count = int(input('반복할 횟수를 입력하세요 : '))

i = 0

while i < count :
    print('Hello, Supreme', i)
    i += 1

#초기값을 횟수대로 반복하기 2

count = int(input('반복할 횟수를 입력하세요 : '))


while count > 0 :
    print('Hello, Supreme', count)
    count -= 1
