import pygame, random

pygame.init()

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Viborita")

FPS = 20
clock = pygame.time.Clock()

SNAKESIZE = 20

headx = WINDOW_WIDTH//2
heady = WINDOW_HEIGHT//2 + 100

snakedx = 0
snakedy = 0

score = 0

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

font = pygame.font.SysFont('consolas', 32)

title_text = font.render("Viborita", True, BLACK, WHITE)
title_rect = title_text.get_rect()
title_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

score_text = font.render("Score: " + str(score), True, BLACK, WHITE)
score_rect = score_text.get_rect()
score_rect.topleft = (10, 10)

gameover_text = font.render("Game Over", True, RED, WHITE)
gameover_rect = gameover_text.get_rect()
gameover_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2)

continue_text = font.render("Press any key to play again", True, RED, WHITE)
continue_rect = continue_text.get_rect()
continue_rect.center = (WINDOW_WIDTH//2, WINDOW_HEIGHT//2 + 64)

hit = pygame.mixer.Sound("hit.wav")

apple_coord = (500, 500, SNAKESIZE, SNAKESIZE)
head_coord = (headx, heady, SNAKESIZE, SNAKESIZE)
body_coords = []

apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
head_rect = pygame.draw.rect(display_surface,  BLACK, head_coord)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snakedy = 0
                snakedx = -1*SNAKESIZE
            elif event.key == pygame.K_RIGHT:
                snakedy = 0
                snakedx = 1*SNAKESIZE
            elif event.key == pygame.K_UP:
                snakedy = -1*SNAKESIZE
                snakedx = 0
            elif event.key == pygame.K_DOWN:
                snakedy = 1*SNAKESIZE
                snakedx = 0
            elif event.key == pygame.K_a:
                snakedy = 0
                snakedx = -1*SNAKESIZE
            elif event.key == pygame.K_d:
                snakedy = 0
                snakedx = 1*SNAKESIZE
            elif event.key == pygame.K_w:
                snakedy = -1*SNAKESIZE
                snakedx = 0
            elif event.key == pygame.K_s:
                snakedy = 1*SNAKESIZE
                snakedx = 0  

    body_coords.insert(0, head_coord)
    body_coords.pop()

    headx += snakedx
    heady += snakedy
    head_coord = (headx, heady, SNAKESIZE, SNAKESIZE)

    if head_rect.left < 0 or head_rect.right > WINDOW_WIDTH or head_rect.top < 0 or head_rect.bottom > WINDOW_HEIGHT or head_coord in body_coords:
        display_surface.blit(gameover_text, gameover_rect)
        display_surface.blit(continue_text, continue_rect)
        pygame.display.update()

        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    score = 0
                    headx = WINDOW_WIDTH//2
                    heady = WINDOW_HEIGHT//2+100
                    head_coord = (headx, heady, SNAKESIZE, SNAKESIZE)
                    body_coords = []
                    snakedx = 0
                    snakedy = 0
                    is_paused = False                
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False
    
    if head_rect.colliderect(apple_rect):
        score += 1
        hit.play()

        applex = random.randint(0, WINDOW_WIDTH-SNAKESIZE)
        appley = random.randint(0, WINDOW_HEIGHT-SNAKESIZE)
        apple_coord = (applex, appley, SNAKESIZE, SNAKESIZE)

        body_coords.append(head_coord)

    score_text = font.render("Score: " + str(score), True, BLACK, WHITE)
        
    display_surface.fill(WHITE)
    
    display_surface.blit(score_text, score_rect)

    head_rect = pygame.draw.rect(display_surface, BLUE, head_coord)
    apple_rect = pygame.draw.rect(display_surface, RED, apple_coord)
    for body in body_coords:
        pygame.draw.rect(display_surface, BLACK, body)
    
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()