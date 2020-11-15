#while 2

import random

print(random.random())

print(random.randint(1, 6)) #1~6까지의 정수인 난수 생성


#while을 사용한 주사위

import random

i = 0

while i != 3 :
    i = random.randint(1, 6)
    print(i)

#random.choice 활용하기
dice = [1, 2, 3, 4, 5, 6]

print(random.choice(dice))

print(random.choice(dice))

#무한 루프

while True:
    print('Hello')
while 1:
    print('Hello2')
while 'ptyhon':
    print('Hello3')
