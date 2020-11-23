# application_string

# 특정 문자 삭제하기


left = ',  PYTHON  .  '.lstrip(', .') # 문자열 왼쪽에 있는 공백과 콤마와 점 삭제
right = ',  PYTHON  .  '.rstrip(', .') # 문자열 오른쪽에 있는 공백과 콤마와 점 삭제
both = ',  PYTHON  .  '.strip(', .') # 문자열 양쪽에 있는 공백과 콤마와 점 삭제

print(left, right, both, sep='\n')

# 문자열 정렬하기


left_arr = 'python'.ljust(10)  # 총 10칸 중 6칸은 문자열 4칸은 공백
right_arr = 'python'.rjust(10) # 총 10칸 중 6칸은 문자열 4칸은 공백
center_arr = 'python'.center(10) # 총 10칸 중 6칸은 문자열 4칸은 공백

print(left_arr, right_arr, center_arr, sep='\n')


# method chaining

method_chaining = 'python'.rjust(10).upper()
print(method_chaining)

# 문자열 왼쪽에 0 채우기

a = '35'.zfill(4)        # 숫자 앞에 0을 채움

b = '3.5'.zfill(6)       # 숫자 앞에 0을 채움

c = 'hello'.zfill(10)    # 문자열 앞에 0을 채울 수도 있음

print(a, b, c, sep='\n')

# 문자열 위치 찾기

print('apple pineapple'.find('pl'))

print('apple pineapple'.find('xy'))

print('apple pineapple'.rfind('pl'))

print('apple pineapple'.rfind('xy'))

print('apple pineapple'.index('pl'))
print('apple pineapple'.rindex('pl'))

# 문자열 개수 세기

print('apple pineapple'.count('pl'))
