import pygame
import random
import sys

pygame.init()

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
food_weight = random.choice ([1,2,3])
food_timer = pygame.time.get_ticks()
food_lifetime = 5000
score = 0
speed = 5
level = 1

fps = pygame.time.Clock()

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

def corner_text(text, font, color, x,y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(topleft = (x,y))
    screen.blit(text_surface, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

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
        score += food_weight
        food = gen_food()
        food_weight = random.choice([1,2,3])

        food_timer = pygame.time.get_ticks()

        if score % 4 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()

    current_time = pygame.time.get_ticks()

    if current_time - food_timer > food_lifetime:
        food = gen_food()
        food_weight = random.choice([1,2,3])
        food_timer = pygame.time.get_ticks()

    if head_x < 0 or head_x >= w or head_y < 0 or head_y >= h:
        screen.fill(red)
        center_text("GAME OVER", big_font, w, h //2 )
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    if len(snake) != len(set(snake)):
        screen.fill(red)
        center_text("GAME OVER", big_font, w, h // 2)
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()
        sys.exit()

    screen.fill(black)

    for x,y in snake:
        pygame.draw.rect(screen, green, (x,y, cell_size, cell_size))

    if food_weight == 1:
        food_color = (255,0,0)
    elif food_weight == 2:
        food_color = (255,255,0)
    elif food_weight == 3:
        food_color = (180,0,255)

    pygame.draw.rect(screen, food_color, (food[0], food[1], cell_size,cell_size))
    

    corner_text("Score:" + str(score), font, white, 10, 10)
    corner_text("Level:" + str(level), font, white, w - 100, 10)

    pygame.display.update()
    fps.tick(speed)

