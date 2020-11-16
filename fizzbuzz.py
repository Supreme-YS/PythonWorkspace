#Fizz Buzz
for i in range(1, 101):

    if i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
        

    if i % 3 == 0:

        print('Fizz')

    elif i % 5 == 0:

        print('Buzz')

    else:
        print(i)

    
#논리 연산자를 사용하지 않고 Fizz Buzz 문제 풀기

for i in range(1, 101):

    if i % 15 == 0:
        print('FizzBuzz')

    elif i % 3 == 0:
        print('Fizz')

    elif i % 5 == 0:
        print('Buzz')

    else:
        print(i)

#코드 단축을 통한 Fizz Buzz 문제


for i in range(1, 101):
    print('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
