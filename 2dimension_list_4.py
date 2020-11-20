# for로 1차원 리스트 만들기

a = [] # 빈 리스트

for i in range(10):
    a.append(0) # append로 요소 추가

print(a)

# for로 2차원 리스트 만들기

b = [] # 빈 리스트

for i in range(3):
    line = [] # 안쪽 리스트로 사용할 빈 리스트

    for j in range(2):
        
        line.append(0)

    b.append(line)

print(b)

# 리스트 컴프리헨션으로 2차원 리스트 만들기

a = [[0 for j in range(2)] for i in range(3)]

print(a)

# 리스트 컴프리헨션으로 2차원 리스트 만들기 2

b = [[0] * 2 for i in range(3)]

print(b)

# 톱니형 리스트

a = [3, 1, 3, 2, 5]    # 가로 크기를 저장한 리스트

b = []    # 빈 리스트 생성
 
for i in a:      # 가로 크기를 저장한 리스트로 반복
    
    line = []    # 안쪽 리스트로 사용할 빈 리스트 생성
    
    for j in range(i):    # 리스트 a에 저장된 가로 크기만큼 반복
        
        line.append(0)
        
    b.append(line)        # 리스트 b에 안쪽 리스트를 추가
 
print(b)

# 톱니형 리스트 (comprehension)

a = [[0] * i for i in [3, 1, 3, 2, 5]]

print(a)
