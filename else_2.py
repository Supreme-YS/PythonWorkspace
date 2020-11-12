#else

x = 5

if x == 10:
    print('x는 10')

else:
    print('x에 들어있는 숫자는')
    print('10이 아닙니다.')


# 값으로 if , else 동작

if True:
    print('참')    # True는 참
else:
    print('거짓')
 
if False:
    print('참')
else:
    print('거짓')    # False는 거짓
 
if None:
    print('참')
else:
    print('거짓')    # None은 거짓


# 조건문에 숫자 지정하기

if 0:
    print('참')
else:
    print('거짓')    # 0은 거짓
 
if 1:
    print('참')    # 1은 참
else:
    print('거짓')
 
if 0x1F:    # 16진수
    print('참')    # 0x1F는 참
else:
    print('거짓')
 
if 0b1000:    # 2진수
    print('참')    # 0b1000은 참
else:
    print('거짓')
 
if 13.5:    # 실수
    print('참')    # 13.5는 참
else:
    print('거짓')


#if 조건문에 문자열 지정하기

if 'Hello':    # 문자열
    print('참')    # 문자열은 참
else:
    print('거짓')
 
if '':    # 빈 문자열
    print('참')
else:
    print('거짓')    # 빈 문자열은 거짓


#not
if not 0:
    print('참')    # not 0은 참
 
if not None:
    print('참')    # None은 참
 
if not '':
    print('참')    # not 빈 문자열은 참

#조건식을 여러개 지정하기
x = 10
y = 20
 
if x == 10 and y == 20:     # x가 10이면서 y가 20일 때
    print('참')
else:
    print('거짓')

#조건식을 여러개 지정하기

if x > 0:
    if x < 20:
        print('20보다 작은 양수')

#보다 간단한 방법
if x > 0 and x < 20:
    print('20보다 작은 양수입니다.')

#더욱 간단한 방법
if 0 < x < 20:
    print('20보다 작은 양수입니다.')
