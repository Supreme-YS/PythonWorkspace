#sequence_types
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(10 in a)
print(11 in a)

b = list(range(11))
print(10 not in b)
print(11 not in b)

print('P' in 'Hello, Python')

c = [0, 10, 20, 30]
d = [9, 8, 7, 6]
print(c + d) 

#error_range
#range(0, 10) + range(10, 20) << - make a error so we have to do something
#we can change these ranges to tuple or list

e = list(range(0, 10)) + list(range(10, 20))
print(e)

f = tuple(range(0, 10)) + tuple(range(10, 20))
print(f)

#attach_string
string = 'Hello, ' + 'Python!'
print(string)

#string + number
#'Hello, ' + 10 << - make a error

string2 = 'hello, ' + str(10) #str을 사용하여 정수를 문자열로 변환
string3 = 'hello, ' + str(1.5) #str을 사용하여 실수를 문자열로 변환
print(string2, string3, sep='\n')

#repeat_sequence
print([0, 10, 20, 30] * 3) #요소 0, 10, 20, 30이 들어있는 리스트를 3번 반복한다.

print(list(range(0, 3)) * 3)
print(tuple(range(0, 3)) * 3)

#repeat_string
print('Hello, Python' * 3)
