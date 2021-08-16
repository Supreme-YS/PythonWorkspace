#list_comprehension

a = [i for i in range(10)] # 0부터 9까지 숫자를 생성하여 리스트 생성

print(a)

b = list(i for i in range(10)) # 0부터 9까지 숫자를 생성하여 리스트 생성

print(b)

c = [i + 5 for i in range(10)] # 0부터 9까지 숫자를 생성하면서 값에 5를 더하여 리스트 생성

print(c)


d = list(i + 5 for i in range(10))  # 0부터 9까지 숫자를 생성하면서 값에 5를 더하여 리스트 생성

print(d)
