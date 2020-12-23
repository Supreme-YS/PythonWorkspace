# 300 challenge_1

# 11
# 삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.

삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

# 12

시가총액 = 298000000000000
현재가 = 50000
PER = 15.79

print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

# 13 # hello! python 출력하기

s = "Hello"
t = "Python"

print(s+"!"+t) #이건 정답이 아니다
print(s+"!",t) #이것이 정답이다. # ,(콤마)를 사용하면 자동으로 1 space 확보

# 14 2 + 2 * 3의 실행결과

print(2 + 2 * 3)

# 15

a = 128
print(type(a))

# 16 문자열을 정수형으로 변환

num_str = "720" 
num_int = int(num_str) #int(정수형)으로 형태를 변경하고, num_int라는 새로운 변수에 할당
print(type(num_str))
print(num_int+1, type(num_int))
