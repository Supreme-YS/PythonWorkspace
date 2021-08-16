#문자열 사용하기
hello = 'hello, world!'
hello2 = "hello, world!"
hello3 = '''hello, world!'''
hello4 = """hello, world!"""
print(hello, hello2, hello3, hello4, sep='\n')

#문자열 규칙
#문자열 안에 (작은따옴표)를 넣고싶다면 (큰따옴표)로 묶기

string1 = "'Hello, Python'"
print(string1)

string2 = '"Hello, Python"'
print(string2)

single_quote = '''"안녕하세요."
'파이썬'입니다.'''
 
double_quote1 = """"Hello"
'Python'"""
 
double_quote2 = """Hello, 'Python'"""    # 한 줄로 작성
 
print(single_quote)
print(double_quote1)
print(double_quote2)
