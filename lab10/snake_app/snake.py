import pygame
import random
import sys
from snake_user import save_progress, login_user, create_tables

pygame.init()

create_tables()
user_id, level, score = login_user()

w = 600
h = 400
cell_size = 20
screen = pygame.display.set_mode((w,h))
pygame.display.set_caption("Snake")

black = (0,0,0)
green = (0,200,0)
red = (200,0,0)
white = (255,255,255)

font = pygame.font.SysFont("Verdana", 20)
big_font = pygame.font.SysFont("Verdana", 50)

snake = [(100,100), (80,100), (60,100)]
direction = "RIGHT"
food = (200,100)
fps = pygame.time.Clock()

paused = False   


def gen_food():
    while True:
        new_food = (
            random.randrange(0, w, cell_size),
            random.randrange(0, h, cell_size),
        )
        if new_food not in snake:
            return new_food
        
def center_text(text, font, color, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center = (w // 2, y))
    screen.blit(text_surface, text_rect)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_progress(user_id, level, score)   
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                paused = not paused

                if paused:
                    save_progress(user_id, level, score)

    if paused:
        screen.fill(black)
        center_text("PAUSED", big_font, white, h // 2)
        center_text("Press P to continue", font, white, h // 2 + 40)
        pygame.display.update()
        continue

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and direction != "DOWN":
        direction = "UP"
    if keys[pygame.K_DOWN] and direction != "UP":
        direction = "DOWN"
    if keys[pygame.K_LEFT] and direction != "RIGHT":
        direction= "LEFT"
    if keys[pygame.K_RIGHT] and direction != "LEFT":
        direction = "RIGHT"

    head_x , head_y = snake[0]
    if direction == "UP":
        head_y -= cell_size
    if direction == "DOWN":
        head_y += cell_size
    if direction == "LEFT":
        head_x -= cell_size
    if direction == "RIGHT":
        head_x += cell_size

    new_head = (head_x, head_y)
    snake.insert(0, new_head)

    if snake[0] == food:
        score += 1
        food = gen_food()

        if score % 4 == 0:
            level += 1
    else:
        snake.pop()

    if head_x < 0 or head_x >= w or head_y < 0 or head_y >= h:
        save_progress(user_id, level, score)
        screen.fill(red)
        center_text("GAME OVER", big_font, white, h //2 )
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    if len(snake) != len(set(snake)):
        save_progress(user_id, level, score)
        screen.fill(red)
        center_text("GAME OVER", big_font, white, h // 2)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    screen.fill(black)

    for x,y in snake:
        pygame.draw.rect(screen, green, (x,y, cell_size, cell_size))

    pygame.draw.rect(screen, red, (food[0], food[1], cell_size, cell_size))

    score_text = font.render(f"Score: {score}", True, white)
    level_text = font.render(f"Level: {level}", True, white)

    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (w - 120, 10))

    pygame.display.update()
    fps.tick(7 + level*1)