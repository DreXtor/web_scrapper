import pygame

pygame.init()   # 초기화(반드시 필요!!)

# 화면 크기 설정
screen_width = 480      # 가로 크기
screen_height = 640      # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))    # 창 세팅

# 화면 타이틀 설정
pygame.display.set_caption("Nado Game")     # 게임 이름

# 배경 이미지 불러오기 : pygame.image.load(경로)
background = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/background.jpg")

# 캐릭터(스프라이트) 불러오기
character = pygame.image.load(
    "/Users/iwongi/Desktop/learn_python/nado_coding/make_python_game/pygame_basic/character.png")
character_size = character.get_rect().size   # 캐릭터 이미지 크기
character_width = character_size[0]           # 캐릭터 가로 크기
character_height = character_size[1]          # 캐릭터 세로 크기
character_X_position = (screen_width / 2)-(character_width / 2)    # 캐릭터의 X 좌표
character_Y_position = screen_height - character_height         # 캐릭터의 Y 좌표

#  이벤트 루프가 계속 실행중이어야 창이 꺼지지않는다
# 이벤트 루프
running = True
while running:  # 게임이 진행중인가?
    for event in pygame.event.get():        # 어떤 이벤트가 발생했는가?
        if event.type == pygame.QUIT:       # 창이 닫히는 이벤트가 발생했는가?
            running = False                 # 게임이 진행중이 아님

    # screen.fill((0, 0, 255))               # 단색으로 배경 채우기
    screen.blit(background, (0, 0))         # 배경 그리기

    screen.blit(character, (character_X_position, character_Y_position)) # 캐릭터 그리기
    

    pygame.display.update()                 # 게임화면 다시 그리기 / 계속해서 그려줘야 보여진다


# pygame 종료
pygame.quit()