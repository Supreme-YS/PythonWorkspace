#elif

x = 20

if x == 10:
    print('10 입니다.')

elif x == 20:
    print('20 입니다.')

# 10, 20이 아니라면 elif, if, else, 사용하면 된다.

x = 30

if x == 10:
    print('10 입니다.')

elif x == 20:
    print('20 입니다.')

else:
    print('10도 20도 아닙니다.')

#if 와 elif를 이용하여 자판기 만들기

button = int(input())

if button == 1:
    print('콜라')

elif button == 2:
    print('사이다')

elif button == 3:
    print('환타')

else:
    print('제공하지 않는 메뉴')
