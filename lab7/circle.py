import pygame

pygame.init()

width, height = 800, 600
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("RED BALL")

radius = 25
x = width // 2
y = height // 2
speed = 20
color = (255,0,0)
bg = (255,255,255)

run = True 
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        if y - radius - speed >= 0:
            y -= speed

    if keys[pygame.K_DOWN]:
        if y + radius + speed <= height:
            y += speed

    if keys[pygame.K_LEFT]:
        if x - radius - speed >= 0:
            x -= speed

    if keys[pygame.K_RIGHT]:
        if x + radius + speed <= width:
            x += speed

    screen.fill(bg)
    pygame.draw.circle(screen, color, (x,y), radius)
    pygame.display.flip()


pygame.quit()