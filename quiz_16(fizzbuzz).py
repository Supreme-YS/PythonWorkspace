#practice_fizzbuzz
#다음 소스 코드를 완성하여 1부터 100까지의 숫자를 출력하면서 2의 배수일 때는 'Fizz', 11의 배수일 때는 'Buzz', 2과 11의 공배수일 때는 'FizzBuzz'가 출력되게 만드세요.


for i in range(1, 101):

    if i % 2 == 0 and i % 11 == 0:
        print('FizzBuzz')

    elif i % 2 == 0:
        print('Fizz')

    elif i % 11 == 0:
        print('Buzz')

    else:
        print(i)


# 골프 코드를 활용해보기

for i in range(1, 101):
    print('Fizz' * (i % 2 == 0) + 'Buzz' * (i % 11 == 0) or i)
