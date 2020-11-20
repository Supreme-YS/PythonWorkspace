# 반복문을 사용한 2차원 리스트 출력
# for 1번
a = [[10, 20], [30, 40], [50, 60]]

for x, y in a:
    print(x, y)
  
# for 2번

a = [[10, 20], [30, 40], [50, 60]]

for i in a:
    for j in i:

        print(j, end = ' ')

    print()

# for 와 range 사용하기


a = [[10, 20], [30, 40], [50, 60]]
 
for i in range(len(a)):            # 세로 크기
    for j in range(len(a[i])):     # 가로 크기
        print(a[i][j], end=' ')
    print()

# while 1번

a = [[10, 20], [30, 40], [50, 60]]

while i < len(a): # 반복할 때 리스트의 크기 활용(세로 크기)
    x, y = a[i] # 요소 두 개를 한꺼번에 가져오기
    print(x, y) 
    i += 1 # 인덱스를 1 증가시킴

# while 2번

a = [[10, 20], [30, 40], [50, 60]]
 
i = 0
while i < len(a):           # 세로 크기
    j = 0
    while j < len(a[i]):    # 가로 크기
        print(a[i][j], end=' ')
        j += 1              # 가로 인덱스를 1 증가시킴
    print()
    i += 1                  # 세로 인덱스를 1 증가시킴

# 잘못된 방법
i = 0
while i < len(a):
    j = 0
    while j < len(a[i]):
        print(a[i][j], end=' ')
        j += 1
        i += 1    # 안쪽 while에서 i를 증가시키면 안 됨. 잘못된 방법
    print()
