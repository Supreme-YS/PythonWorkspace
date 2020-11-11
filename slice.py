#slicing
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[0:4]) # 인덱스 0부터 3까지 잘라서 새 리스트를 만듦
print(a[0:11])

print(a[1:1]) # 인덱스 1부터 0까지 잘라서 새 리스트를 만듦
print(a[1:2]) # 인덱스 1부터 1까지 잘라서 새 리스트를 만듦
print(a[4:7]) # 인덱스 4부터 6까지 요소 3개를 가져옴


#negative_slice
print(a[4:-1])

#인덱스 증가폭

print(a[2:8:3]) # 인덱스 2부터 3씩 증가시키면서 인덱스 7까지 가져옴
print(a[2:9:3]) # 인덱스 2부터 3씩 증가시키면서 인덱스 8까지 가져옴

#인덱스 생략

print(a[:7]) # 리스트 처음부터 인덱스 6까지 가져옴
print(a[7:]) # 인덱스 7부터 마지막 요소까지 가져옴

#리스트 전체 가져오기
print(a[:])

#인덱스 생략하면서 증가폭 사용
print(a[:7:2]) # 리스트의 처음부터 인덱스를 2씩 증가시키면서 인덱스 6까지 가져옴

print(a[7::2]) # 인덱스 7부터 2씩 증가시키면서 리스트의 마지막 요소까지 가져옴

print(a[::2]) # 리스트 전체에서 인덱스 0부터 2씩 증가시키면서 요소를 가져옴

#negative

print(a[5:1:-1]) #리스트 a에서 인덱스 5부터 2까지 1씩 감소시키면서 요소를 가져옴
print(a[::-1]) #리스트 순서 뒤집기

#len을 이용한 전체 리스트 가져오기
print(a[0:len(a)])
print(a[:len(a)])

#튜플, range, 문자열에 슬라이스 사용하기
#tuple
b = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
print(b[4:7]) #인덱스 4부터 6까지 요소 3개를 가져옴
print(b[4:]) #인덱스 4부터 마지막 요소까지 가져옴
print(b[:7:2]) #튜플의 처음부터 인덱스를 2씩 증가시키면서 6까지 가져옴

#range
r = range(10)
range(0, 10)
print(r[4:7])     # 인덱스 4부터 6까지 숫자 3개를 생성하는 range 객체를 만듦
range(4, 7)
print(r[4:])      # 인덱스 4부터 9까지 숫자 6개를 생성하는 range 객체를 만듦
range(4, 10)
print(r[:7:2])    # 인덱스 0부터 2씩 증가시키면서 인덱스 6까지 숫자 4개를 생성하는 range 객체를 만듦
range(0, 7, 2)

#range 객체들을 list로 만들기 위해서 list에 넣어줘야 한다.

print(list(range(0, 10)))
print(list(r[4:7])) 
print(list(range(4, 7)))
print(list(r[4:]))     
print(list(range(4, 10)))
print(list(r[:7:2]))    
print(list(range(0, 7, 2)))

#문자열 slicing

hello = 'Hello, world!'
print(hello[2:9])    # 인덱스 2부터 인덱스 8까지 잘라서 문자열을 만듦
print(hello[2:])     # 인덱스 2부터 마지막 요소까지 잘라서 문자열을 만듦
print(hello[:9:2])   # 문자열의 처음부터 인덱스를 2씩 증가시키면서 인덱스 8까지 잘라서 문자열을 만듦

#slice 객체 사용하기

range(10)[slice(4, 7, 2)]
range(10).__getitem__(slice(4, 7, 2))

#slice 객체를 하나만 만든 뒤 여러 시퀀스에 적용하기
s = slice(4, 7) # 인덱스 4부터 6까지 자르는 slice 객체 생성
print(a[s])
r = range(10)
print(list(r[s])) #r은 위에서 range로 정의했기 때문에 list에 삽입을 해줘야 범위 출력이 아닌 값이 출력
print(hello[s])

