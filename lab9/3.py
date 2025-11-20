import pygame
import sys

def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    
    radius = 15
    mode = 'blue'
    tool = 'brush'
    
    while True:
        
        pressed = pygame.key.get_pressed()
        
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
            
                if event.key == pygame.K_r:
                    mode = 'red'
                elif event.key == pygame.K_g:
                    mode = 'green'
                elif event.key == pygame.K_b:
                    mode = 'blue'
                elif event.key == pygame.K_p:
                    mode = 'pink'

                elif event.key == pygame.K_1:
                    tool = 'brush'
                elif event.key == pygame.K_2:
                    tool = 'rect'
                elif event.key == pygame.K_3:
                    tool = 'circle'
                elif event.key == pygame.K_4:
                    tool = 'eraser'
                elif event.key == pygame.K_5:
                    tool = 'square'
                elif event.key == pygame.K_6:
                    tool = 'right_triangle'
                elif event.key == pygame.K_7:
                    tool = 'equilateral_triangle'
                elif event.key == pygame.K_8:
                    tool = 'rhombus'
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tool == 'rect':
                    draw_rect(screen, event.pos, radius, mode)

                if tool == 'circle':
                    draw_circle(screen, event.pos, radius, mode)

                if tool == 'square':
                    draw_square(screen, event.pos, radius, mode)

                if tool == 'right_triangle':
                    draw_right_triangle(screen, event.pos, radius, mode)

                if tool == 'equilateral_triangle':
                    draw_equilateral_triangle(screen, event.pos, radius, mode)

                if tool == 'rhombus':
                    draw_rhombus(screen, event.pos, radius, mode)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    radius = min(200, radius + 1)
                elif event.key == pygame.K_DOWN:
                    radius = max(1, radius - 1)        
            
            if event.type == pygame.MOUSEMOTION:
                position = event.pos

                if tool == 'brush':
                    pygame.draw.circle(screen, get_color(mode), position, radius)

                elif tool == 'eraser':
                    pygame.draw.circle(screen, (0,0,0), position, radius)
        
        pygame.display.flip()
        clock.tick(60)


def draw_rect(screen, position, radius, color_mode):
    color = get_color(color_mode)
    x, y = position

    size = radius * 2
    rect = pygame.Rect(x - radius, y - radius, size, size)
    pygame.draw.rect(screen, color, rect, 2)

def draw_circle(screen, position, radius, color_mode):
    color = get_color(color_mode)
    x, y = position

    pygame.draw.circle(screen, color, (x, y), radius, 2)

def draw_square(screen,position,radius,color_mode):
    color = get_color(color_mode)
    x, y = position
    side = radius * 2 
    rect = pygame.Rect (x-radius, y - radius, side, side)
    pygame.draw.rect(screen, color, rect, 2)

def draw_right_triangle(screen, position, radius, color_mode):
    color = get_color(color_mode)
    x, y = position

    p1 = (x, y)
    p2 = (x + radius, y)
    p3 = (x, y - radius)

    pygame.draw.polygon(screen, color, [p1, p2, p3], 2)

def draw_equilateral_triangle(screen, position, radius, color_mode):
    color = get_color(color_mode)
    x, y = position

    p1 = (x, y - radius)
    p2 = (x - radius, y + radius)
    p3 = (x + radius, y + radius)

    pygame.draw.polygon(screen, color, [p1, p2, p3], 2)

def draw_rhombus(screen, position, radius, color_mode):
    color = get_color(color_mode)
    x, y = position
    
    top = (x, y - radius)
    bottom = (x, y + radius)
    left = (x - radius, y)
    right = (x + radius, y)

    pygame.draw.polygon(screen, color, [top, right, bottom, left], 2)

def get_color(color_mode):
    if color_mode == 'red':
        return (255, 0, 0)
    elif color_mode == 'green':
        return (0, 255, 0)
    elif color_mode == 'blue':
        return (0, 0, 255)
    elif color_mode == 'yellow':
        return (255, 255, 0)
    elif color_mode == 'pink':
        return (255, 105,180)
    else:
        return (0, 0, 0)

main()
