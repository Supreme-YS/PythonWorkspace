#clear, slicing control

a = [10, 20, 30]

a.clear()


a[len(a):] = [500] # append와 같은 효과

print(a)

a[len(a):] = [500, 600] # extend와 같은 효과

print(a)

# 빈 리스트 확인하기

if not len(seq): # 리스트가 비어 있으면 True
if len(seq): # 리스트에 요소가 있으면 True

if not seq: # 리스트가 비어 있으면 True
if seq: # 리스트에 내용이 있으면 True
