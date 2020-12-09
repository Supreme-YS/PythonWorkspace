# 주민등록번호를 기반으로 한 성별 구분하기

id_num = input('주민등록번호를 입력하세요 : ')

print(id_num)

if id_num[7] == '1' or id_num[7] == '3':
    
    print("남자입니다.")
    
else:
    print("여자입니다.")

