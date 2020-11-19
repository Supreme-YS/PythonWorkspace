# 가장 작은 수 구하기

a = [1, 2, 3, 4, 5]

smallest = a[0]

for i in a:
    if i < smallest:
        smallest = i

print(smallest)

# 가장 큰 수 구하기

a = [100, 2, 35, 50, 80]

largest = a[0]

for i in a:
    if i > largest:
        largest = i


print(largest)


# sort

a = [100, 2, 35, 50, 80]
a.sort() # default 값 오름차순(ASC)

print(a[0]) 

a.sort(reverse=True) # 오름차순의 역순 (=내림차순, DESC)

print(a[0])


# min, max 활용

a = [100, 2, 35, 50, 80]

print(min(a))
print(max(a))
