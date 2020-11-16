# 5 X 5 별상자 만들기

for i in range(5):          # 5번 반복, 바깥쪽 i는 세로방향

    for j in range(5):      # 5번 반복, 안쪽 j는 가로방향

        print('*', end='')  # 별 출력, end에 ''를 지정하여 줄바꿈을 하지 않음
 
    print()                 # 가로 방향으로 별을 다 그린 뒤 다음 줄로 넘어감
        
# 3 X 7 별상자 만들기

for i in range(3):

    for j in range(7):

        print('★', end='')

    print()
