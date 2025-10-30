import pygame
import os

pygame.init()
pygame.mixer.init()

music = "/Users/adelkikbai/Desktop/code/pp2/lab7/music"

playlist = []
for f in os.listdir(music):
    if f.endswith(".mp3"):
        playlist.append(f)

print(playlist)

index = 0 
pygame.mixer.music.load(os.path.join(music, playlist[index]))

screen = pygame.display.set_mode((1000,400))
pygame.display.set_caption("music player")
font = pygame.font.Font(None, 36)

def design(text, x, y):
    render = font.render(text, True, (255,255,255))
    screen.blit(render, (x,y))

def play_music(index):
    if playlist:
        pygame.mixer.music.load(os.path.join(music, playlist[index]))
        pygame.mixer.music.play()
        print(f"playing: {playlist[index]}")

if playlist:
    play_music(index)
else:
    print("No music files found in the folder.")

run = True 
while run:
    screen.fill((0,0,0))
    design("music player", 120, 20)

    if playlist:
        design(f"now playing: {playlist[index]}", 250,100)
    else:
        design(f"no music files found", 50, 100)
    
    design("P: play", 100,150)
    design("S: stop", 100, 180)
    design("N: next", 100,210)
    design("B: back", 100,240)
    design("ESC: Exit", 100,270)

    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                pygame.mixer.music.play()
                print(playlist[index])

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                print("stopped")

            elif event.key == pygame.K_n:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(os.path.join(music, playlist[index]))
                pygame.mixer.music.play()
                print("next", playlist[index])

            elif event.key == pygame.K_b:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(os.path.join(music, playlist[index]))
                pygame.mixer.music.play()
                print("previous", playlist[index])

            elif event.key == pygame.K_ESCAPE:
                run = False



pygame.quit()
