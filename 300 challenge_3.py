# 300 challenge

# 21 letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.

letters = 'python'
print(letters[0], letters[2])

# 22 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.

license_plate = "24가 2210"
print(license_plate[-4:])

# 23 아래의 문자열에서 '홀' 만 출력하세요.

string = "홀짝홀짝홀짝"
print(string[0:6:2])
print(string[::2])

# 24 문자열을 거꾸로 뒤집어 출력하세요.

string = "PYTHON"
print(string[::-1])

# 25 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.

phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", " ")
print(phone_number1)

# 26 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.

phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-", "")
print(phone_number1)

# 27 url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.

url = "http://sharebook.kr"
print(url[-2:]) #슬라이싱 방법

url_split = url.split('.')
print(url_split)
print(url_split[1], url_split[-1])

# 28 문자열은 immutable 아래 코드의 실행 결과를 예상해보세요.

lang = 'python'
#lang[0] = 'P' # 문자열은 수정할 수 없다. Immutable
print(lang) 

# 29 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.

string = 'abcdfe2a354a32a'
string_replace = string.replace('a', 'A')
print(string_replace)

# 30 아래 코드의 실행 결과를 예상해보세요.

string = 'abcd'
string.replace('b', 'B')
print(string)
# abcd가 그대로 출력됩니다. 왜냐하면 문자열은 변경할 수 없는 자료형이기 때문입니다. replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해줍니다.



