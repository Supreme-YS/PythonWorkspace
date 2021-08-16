#if

x = 10
if x == 10:
    print('10 입니다')


y = 10
if y == 10:
    pass #TODO : x가 10일 때 처리가 필요

#x = 10
#if x == 10:
#    print('x에 들어있는 숫자는')
#        print('10 입니다.') # unexpected indent 에러 발생

x = 10
if x == 10:
    print('x에 들어있는 숫자는')
    print('10 입니다.') # 들여쓰기를 같게 해야한다.


x = 5 # x에 5를 할당
if x == 10: # x값이 5이므로 조건식을 만족하지 않는다.
    print('x에 들어있는 숫자는')
    
print('10 입니다') # 위의 if와는 상관없는 코드

#if와 들여쓰기 칸 수

x = 10

if x == 10:
    print('x에 들어있는 숫자는')
    print('10 입니다')
