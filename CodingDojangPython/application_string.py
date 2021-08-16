# 문자열 바꾸기

word = 'Hello, world'.replace('world', 'Python')
print(word)


# 문자 바꾸기

table = str.maketrans('aeiou', '12345')
word2 = 'apple'.translate(table)

print(word2)

# 문자열 분리하기

fruits = 'apple pear grape pineapple orange'.split()
print(fruits)

# 구분자 문자열과 문자열 리스트 연결하기
fruits2 = ' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
fruits3 = '-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])

print(fruits2)
print(fruits3)

# 소문자 ↔ 대문자

upper = 'python'.upper()
lower = 'PYTHON'.lower()

print(upper, lower, sep ='\n')


# 공백 삭제하기

left = '    python    '.lstrip()
right = '    python    '.rstrip()
both = '    python    '.strip()

print(left, right, both, sep='\n')
