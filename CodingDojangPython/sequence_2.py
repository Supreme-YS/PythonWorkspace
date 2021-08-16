#sequence2
a = list(range(0, 100, 10))
print(len(a))

b = (38, 76, 43, 6, 2)
print(len(b))

print(len(range(0, 10, 2)))

#string_length

hello = 'hello, python'
print(len(hello))

#korean_length

hello2 = '안녕하세요'
print(len(hello2))

#utf-8 korean_length

hello3 = '안녕하세요'
print(len(hello3.encode('utf-8')))
