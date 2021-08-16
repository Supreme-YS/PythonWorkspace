#sequence3
a = [1, 2, 3 ,4, 5]
print(a[0]) #리스트의 첫 번째 인덱스0 요소 출력
print(a[1]) #리스트의 두 번째 인덱스1 요소 출력
print(a[2]) #리스트의 세 번째 인덱스2 요소 출력
print(a[3]) #리스트의 네 번째 인덱스3 요소 출력
print(a[4]) #리스트의 다섯 번째 인덱스4 요소 출력

b = (38, 21, 53, 62, 19)
print(b[0])        # 튜플의 첫 번째(인덱스 0) 요소 출력

r = range(0, 10, 2)
print(r[2])        # range의 세 번째(인덱스 2) 요소 출력

hello = 'Hello, world!'
print(hello[7])    # 문자열의 여덟 번째(인덱스 7) 요소 출력

#_getitem_ 메서드

a = [38, 21, 53, 62, 19]
print(a.__getitem__(1))

#negative_index
ab = [38, 21, 53, 62, 19]

print(ab[-1])   # 리스트의 뒤에서 첫 번째(인덱스 -1) 요소 출력

print(ab[-5])   # 리스트의 뒤에서 다섯 번째(인덱스 -5) 요소 출력

#error

#print(a[5]) #인덱스 범위 에러 발생 IndexError
print(a[len(a)-  1]) #인덱스 범위 - 1로 a의 마지막 요소 출력

#요소에 값 할당하기

c = [0, 0, 0, 0, 0]
a[0] = 1
a[1] = 2
a[2] = 3
a[3] = 4
a[4] = 5

print(c)

#요소 삭제하기
d = [1, 2, 3, 4, 5]
del d[2] #d의 세번째 객체 값 삭제
print(d)

