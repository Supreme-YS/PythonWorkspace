# #표준 입출력

# print("Python", "Java", sep=",", end="?") #문장의 끝부분(end), default 값은 줄바꿈
# print("무엇이 더 재밌을까요?")

# import sys
# print("Python", "Java", file=sys.stdout)
# print("Python", "Java", file=sys.stderr)

#시험 성적
scores = {"수학" : 0, "영어" : 50, "코딩" : 100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":") #ljust(8) 8공간을 확보하고 왼쪽정렬을 하고 표시 #rjust (4공간을 확보하고 오른쪽 정렬)


#은행 대기순번표
# 001, 002, 003, ...

# for num in range(1, 21):
#     print("대기번호 : " + str(num).zfill(3)) #3크기만큼의 값을 확보하고 나머지에 대해 0으로 채운다

answer = input("아무 값이나 입력하세요 : ") #항상 문자열로 받는다.
print("입력하신 값은 " + answer + "입니다.")
print(type(answer))