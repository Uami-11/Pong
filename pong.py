import sys

import pygame

from Script.Players import Players

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Bad Pong!!")
android18 = pygame.image.load("a18.jpg")
pygame.display.set_icon(android18)
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
fullscreen = False
monitor_size = [1024, 819]
pygame.mouse.set_visible(False)

def DisplayPlayer(fullscreen):
    if fullscreen:
        pong = pygame.Rect(1024/2-10, 819/2, 30, 30)
    else:
        pong = pygame.Rect(380,400,30,30)
    Player1 = Players(fullscreen, pong)

    return Player1


changed = False
Player = DisplayPlayer(fullscreen)




def DisplayMiddle(fullscreen):
    if fullscreen:
        middle_line1 = pygame.Rect((monitor_size[0]/2), 10, 10, 90)
        middle_line2 = pygame.Rect((monitor_size[0]/2), 110, 10, 90)
        middle_line3 = pygame.Rect((monitor_size[0]/2), 210, 10, 90)
        middle_line4 = pygame.Rect((monitor_size[0]/2), 310, 10, 90)
        middle_line5 = pygame.Rect((monitor_size[0]/2), 410, 10, 90)
        middle_line6 = pygame.Rect((monitor_size[0]/2), 510, 10, 90)
        middle_line7 = pygame.Rect((monitor_size[0]/2), 610, 10, 90)
        middle_line8 = pygame.Rect((monitor_size[0]/2), 710, 10, 90)
    else:
        middle_line1 = pygame.Rect(390,10, 10,90)
        middle_line2 = pygame.Rect(390,110, 10,90)
        middle_line3 = pygame.Rect(390,210, 10,90)
        middle_line4 = pygame.Rect(390,310, 10,90)
        middle_line5 = pygame.Rect(390,410, 10,90)
        middle_line6 = pygame.Rect(390,510, 10,90)
        middle_line7 = pygame.Rect(390,610, 10,90)
        middle_line8 = pygame.Rect(390,710, 10,80)

    middle_line = [middle_line1, middle_line2, middle_line3, middle_line4,
               middle_line5, middle_line6, middle_line7, middle_line8]
    return middle_line

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_F8):
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_F4:
                changed = not changed
                if fullscreen:
                    screen = pygame.display.set_mode((screen_width, screen_height))
                    fullscreen = False
                else:
                    screen = pygame.display.set_mode((monitor_size), pygame.FULLSCREEN)
                    fullscreen = True

    screen.fill((30,30,30))
    middle_line = DisplayMiddle(fullscreen)
    for i in range(8):

        pygame.draw.rect(screen, (211,211,211), middle_line[i])
    if not changed:
        Player = DisplayPlayer(fullscreen)
        changed = not changed

    Player.update(screen)


    pygame.display.update()
    clock.tick(60)

