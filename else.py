#else

x = 5
if x == 10:
    print('10입니다')
else:
    print('10이 아닙니다')


x = 5
if x == 10:
    y = x
else:
    y = 0

#축약 & 람다 표현
x = 5
y = x if x == 10 else 0
