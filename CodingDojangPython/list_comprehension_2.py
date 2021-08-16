# list_comprehension_2

# 리스트 표현식에서 if 조건문 사용하기
# 0~9 숫자 중 2의 배수인 숫자(짝수)로 리스트 생성

a = [i for i in range(10) if i % 2 == 0]

print(a)


# 0~9 숫자 중 홀수를 생성하고 그 값에 5를 곱한 값으로 리스트 생성

b = [ i * 5 for i in range(10) if i % 2 == 1]

print(b)

# gu-gu-dan

c = [ i * j for j in range(2, 10) for i in range(1, 10) ]

print(c)

# gu-gu-dan clear


d = [ i * j for i in range(2, 10)
            for j in range(1, 10)]


