# quiz_review_4

# 표준 입력으로 국어, 영어, 수학, 과학 점수가 입력됩니다. 평균 점수를 출력하는 프로그램을 만드세요(input에서 안내 문자열은 출력하지 않아야 합니다). 단, 평균 점수를 출력할 때는 소수점 이하 자리는 버립니다(정수로 출력).

korean, english, math, science = map(int, input().split())

print(int((korean + english + math + science)/4))

print((korean + english + math + science)//4)
