import pygame
import math
import datetime

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey Clock")
clock = pygame.time.Clock()


leftarm = pygame.image.load("/Users/adelkikbai/Desktop/code/pp2/lab7/images/leftarm.png")
rightarm = pygame.image.load("/Users/adelkikbai/Desktop/code/pp2/lab7/images/rightarm.png")
harm = pygame.image.load("/Users/adelkikbai/Desktop/code/pp2/lab7/images/leftarm.png")
mainclock = pygame.transform.scale(pygame.image.load("/Users/adelkikbai/Desktop/code/pp2/lab7/images/clock.png"), (800, 600))


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    now = datetime.datetime.now()
    s = now.second
    m = now.minute
    h = now.hour

    s_angle = s * 6
    m_angle = m * 6 + 45

    screen.blit(mainclock, (0,0))

    rotated_rightarm = pygame.transform.rotate(
        pygame.transform.scale(rightarm, (800,600)), 
        -m_angle
    )
    rightarmrect = rotated_rightarm.get_rect(center = (800 // 2, 600 // 2))
    screen.blit(rotated_rightarm, rightarmrect)

    rotated_leftarm = pygame.transform.rotate(
        pygame.transform.scale(leftarm, (40.95, 682.5)),
        -s_angle
    )
    leftarmrect = rotated_leftarm.get_rect(center = (800 // 2 , 600 // 2))
    screen.blit(rotated_leftarm, leftarmrect)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
