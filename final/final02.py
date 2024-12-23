import pygame
import random

# 初始化 pygame
pygame.init()

# 視窗大小
WIDTH, HEIGHT = 400, 600

# 顏色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (135, 206, 250)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# 建立視窗
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("飛行小鳥遊戲")

# 時鐘
clock = pygame.time.Clock()

# 字型
font = pygame.font.SysFont("comicsansms", 35)

def display_score(score):
    value = font.render("分數: " + str(score), True, BLACK)
    screen.blit(value, [10, 10])

def game_loop():
    # 小鳥參數
    bird_x = 50
    bird_y = HEIGHT // 2
    bird_size = 20
    bird_velocity = 0
    gravity = 0.5
    jump = -10

    # 障礙物參數
    pipe_width = 50
    pipe_gap = 150
    pipe_x = WIDTH
    pipe_height_top = random.randint(50, HEIGHT - pipe_gap - 50)
    pipe_height_bottom = HEIGHT - pipe_gap - pipe_height_top
    pipe_speed = 5

    # 分數
    score = 0

    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird_velocity = jump

        # 更新小鳥位置
        bird_velocity += gravity
        bird_y += bird_velocity

        # 更新障礙物位置
        pipe_x -= pipe_speed
        if pipe_x + pipe_width < 0:
            pipe_x = WIDTH
            pipe_height_top = random.randint(50, HEIGHT - pipe_gap - 50)
            pipe_height_bottom = HEIGHT - pipe_gap - pipe_height_top
            score += 1

        # 碰撞檢測
        if bird_y < 0 or bird_y + bird_size > HEIGHT:
            game_over = True
        if (pipe_x < bird_x + bird_size < pipe_x + pipe_width or 
            pipe_x < bird_x < pipe_x + pipe_width):
            if bird_y < pipe_height_top or bird_y + bird_size > HEIGHT - pipe_height_bottom:
                game_over = True

        # 繪製遊戲畫面
        screen.fill(BLUE)
        pygame.draw.rect(screen, GREEN, [pipe_x, 0, pipe_width, pipe_height_top])  # 上管道
        pygame.draw.rect(screen, GREEN, [pipe_x, HEIGHT - pipe_height_bottom, pipe_width, pipe_height_bottom])  # 下管道
        pygame.draw.circle(screen, RED, (bird_x, bird_y), bird_size // 2)  # 小鳥
        display_score(score)

        pygame.display.update()
        clock.tick(30)

    # 遊戲結束畫面
    screen.fill(WHITE)
    game_over_text = font.render("遊戲結束! 分數: " + str(score), True, BLACK)
    screen.blit(game_over_text, [WIDTH // 6, HEIGHT // 3])
    restart_text = font.render("按 R 重新開始", True, BLACK)
    screen.blit(restart_text, [WIDTH // 6, HEIGHT // 2])
    pygame.display.update()

    # 等待重新開始或退出
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    game_loop()

# 啟動遊戲
game_loop()
