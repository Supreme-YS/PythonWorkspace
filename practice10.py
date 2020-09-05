#문자열처리함수

python = "Python is Amazing"
print(python.lower()) #다 소문자로 만드는 거
print(python.upper()) #모든 문자 대문자로 출력
print(python[0].isupper()) #python의 첫번째(0)문자가 대문자냐?(isupper)
print(len(python)) #문자의 길이
print(python.replace("Python", "Java")) #특정 문자 치환


index = python.index("n") #첫번째 n을 찾을 것이다.
print(index)
index = python.index("n", index + 1) #두번째 n을 찾을 것이다.
print(index)

print(python.find("Java"))  #원하는 값이 없으면 -1 반환
#print(python.index("Java")) #index를 쓰면 오류가 난다.


print(python.count("n")) #문자열에서 n이 몇번 나오는지 체크하는 함수