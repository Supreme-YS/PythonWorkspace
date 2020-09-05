# 추첨프로그램


# 댓글 20명 아이디 1~20
# 내용과 상관없이 무작위로 추첨하되 중복 불가
# random 모듈의 shuffle과 sample을 활용



from random import *
users = range(1, 21, 1) #1부터 20까지 숫자를 생성
users = list(users)
#print(type(users))
#print(users)

shuffle(users)
print(users)

winners = sample(users, 4) #4명 중에서 1명은 치킨, 3명은 커피

print(" - - 당첨자 발표 - - ")
print("치킨 당첨자 : {0}".format(winners[0]))
print("커피 당첨자 : {0}".format(winners[1:]))
print(" - - 축하합니다. - - ")