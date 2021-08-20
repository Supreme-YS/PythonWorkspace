#continue 와 break
absent = [2, 5] #결석
no_book = [7] #책을 가져오지 않음
for student in range(1, 11) : #1~10까지
    if student in absent:
        continue #스킵 후 반복문 지속시킴
    elif student in no_book :
        print("오늘 수업 여기까지. {0}는 교무실로 따라와".format(student))
        break #상황에서 반복문을 종료
    print("{0}야, 책을 읽어줘".format(student))
