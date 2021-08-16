#for를 이용한 리스트 값 출력

a = [1, 2, 3, 4, 5]

for i in a:
    print(i)

for i in a:
    print(i, end=' ')

    
for i in [1, 2, 3, 4, 5]:
    print(i)

# index, value 동시 출력

a = [38, 21, 53, 62, 19]

for index, value in enumerate(a):
    print(index, value)
    
for index, value in enumerate(a, start = 1):
    print(index, value)
