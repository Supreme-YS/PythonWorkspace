import turtle as t

n = 60 # 원을 60번 그림

t.shape('turtle')
t.speed('fast') # 그리는 속도를 가장 빠르게 설정

for i in range(n):
    t.circle(120)  #반지름이 120인 원을 그림
    t.right(360 / n) #오른쪽으로 6도 회전
    

