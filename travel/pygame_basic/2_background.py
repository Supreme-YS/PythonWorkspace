import pygame

pygame.init() #초기화 작업 (반드시 필요)

# 화면 크기 설정 (게임 화면 크기 정의)
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("YoungSeok GAME") #게임 이름

# 배경 이미지 불러오기
background = pygame.image.load("C:\\Users\\1234\\Desktop\\PythonWorkspace\\PythonWorkspace\\pygame_basic\\background.png")

# 이벤트 루프 (창이 꺼지지 않도록)

running = True # 게임이 진행중인가?
while running:
    for event in pygame.event.get(): # 동작(키보드, 마우스)을/이벤트가 발생하였는가?
        if event.type == pygame.QUIT: # 창이 닫히는 이벤트가 발생하였는가?
            running = False #게임이 진행중이 아님
    
    # screen.fill((0, 0, 255)) #RGB 값으로 배경 채우기
    
    screen.blit(background, (0, 0)) # 배경 그리기 그리고 X,Y 의 좌표

    pygame.display.update() # 게임 화면을 다시 그리기! 

# pygame 종료
pygame.quit()