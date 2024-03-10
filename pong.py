import sys

import pygame

from Script.Players import Players

#initialising pygame
pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Bad Pong!!")

screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
fullscreen = False
monitor_size = [1024, 819]
pygame.mouse.set_visible(False)

#Displaying the two players at both full screen and normal screen
def DisplayPlayer(fullscreen):
    if fullscreen:
        pong = pygame.Rect(1024/2-10, 819/2, 30, 30)
    else:
        pong = pygame.Rect(380,400,30,30)
    Player1 = Players(fullscreen, pong)

    return Player1

#changed variable to change between full screen and normal
changed = False
#calling function outside of loop to start
Player = DisplayPlayer(fullscreen)




def DisplayMiddle(fullscreen):
    #middle line for full screen
    if fullscreen:
        middle_line1 = pygame.Rect((monitor_size[0]/2), 10, 10, 90)
        middle_line2 = pygame.Rect((monitor_size[0]/2), 110, 10, 90)
        middle_line3 = pygame.Rect((monitor_size[0]/2), 210, 10, 90)
        middle_line4 = pygame.Rect((monitor_size[0]/2), 310, 10, 90)
        middle_line5 = pygame.Rect((monitor_size[0]/2), 410, 10, 90)
        middle_line6 = pygame.Rect((monitor_size[0]/2), 510, 10, 90)
        middle_line7 = pygame.Rect((monitor_size[0]/2), 610, 10, 90)
        middle_line8 = pygame.Rect((monitor_size[0]/2), 710, 10, 90)
    #middle line for normal
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
    #Had to make it global/exctractable
    return middle_line
    

while True:
    for event in pygame.event.get():
        #close with both window button and F8
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_F8):
                pygame.quit()
                sys.exit()
            #fullscreen with F4, like undertale kakaka four frogs
            if event.key == pygame.K_F4:
                changed = not changed
                if fullscreen:
                    screen = pygame.display.set_mode((screen_width, screen_height))
                    fullscreen = False
                else:
                    screen = pygame.display.set_mode((monitor_size), pygame.FULLSCREEN)
                    fullscreen = True

    screen.fill((30,30,30)) #I like this background colour a lot
    middle_line = DisplayMiddle(fullscreen)
    for i in range(8):
        #Displaying all the middle lines wowsers
        pygame.draw.rect(screen, (211,211,211), middle_line[i])
    if not changed:
        #Calling function when screen change
        Player = DisplayPlayer(fullscreen)
        changed = not changed
        #changed so that it is not called for every frame every loop and make players stuck in hell,. It took me too long to figure that out, stupid me!

    Player.update(screen)


    pygame.display.update()
    clock.tick(60)
    #60 frames per second

