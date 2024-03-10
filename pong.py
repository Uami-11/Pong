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


Player1 = Players('1')
Player2 = Players('2')
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

while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_F8):
                pygame.quit()
                sys.exit()
            

    screen.fill((30,30,30))
    for i in range(8):

        pygame.draw.rect(screen, (211,211,211), middle_line[i])
    Player1.update(screen)
    Player2.update(screen)

    pygame.display.update()
    clock.tick(60)

