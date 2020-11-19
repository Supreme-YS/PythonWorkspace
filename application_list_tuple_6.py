#application_list_tuple

a = [0, 0, 0, 0, 0]
b = a 
print(b) # a와 b는 같은 객체
print(a) # a와 b는 같은 객체

print(a is b) # True 출력

# a와 b는 같으므로 리스트 b의 요소를 변경하면 a와 b에 모두 반영됩니다.

b[2] = 99
print(a)

# 완전히 두 개로 분리하기

a = [0, 0, 0, 0, 0]
b = a.copy()

print(a, b)
