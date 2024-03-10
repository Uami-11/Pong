import random

import pygame


class Players(pygame.sprite.Sprite):
    def __init__(self, fullscreen, pong):
        super().__init__()
        if fullscreen:

            self.rect1 = pygame.Rect(50,350, 20,150)
            self.rect2= pygame.Rect(1024-70,350, 20,150)
            self.pong = pygame.Rect(1024/2-10, 819/2, 30, 30)
            self.width = 1024
            self.height = 819
        else:

            self.rect1 = pygame.Rect(50,350, 20,150)
            self.rect2 = pygame.Rect(730,350, 20,150)
            self.pong = pygame.Rect(380,400,30,30)
            self.width = 800
            self.height = 800
        self.pong = pong
        self.pong1 = pong
        self.speed_x = random.choice([5,-5])
        self.speed_y = random.choice([4,-4])

        self.move1 = 0
        self.move2 = 0
        self.fullscreen = fullscreen
        self.count1 = 0
        self.count2 = 0

    def PongMove(self):
        self.pong.bottom += self.speed_y
        self.pong.right += self.speed_x
        if self.pong.bottom >= self.height or self.pong.top <= 0:
            self.speed_y *= -1

    def Collision(self):
        collisiontol = 10
        if self.pong.colliderect(self.rect1):
            if abs(self.rect1.top - self.pong.bottom) < collisiontol and self.speed_y > 0:
                self.speed_y *= -1
            if abs(self.rect1.bottom - self.pong.top) < collisiontol and self.speed_y < 0:
                self.speed_y *= -1
            if abs(self.rect1.right - self.pong.left) < collisiontol and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect1.left - self.pong.right) < collisiontol and self.speed_x > 0:
                self.speed_x *= -1

        if self.pong.colliderect(self.rect2):
            if abs(self.rect2.top - self.pong.bottom) < collisiontol and self.speed_y > 0:
                self.speed_y *= -1
            if abs(self.rect2.bottom - self.pong.top) < collisiontol and self.speed_y < 0:
                self.speed_y *= -1
            if abs(self.rect2.right - self.pong.left) < collisiontol and self.speed_x < 0:
                self.speed_x *= -1
            if abs(self.rect2.left - self.pong.right) < collisiontol and self.speed_x > 0:
                self.speed_x *= -1

    def movement(self):
        keys = pygame.key.get_pressed()
        if self.fullscreen:

            if keys[pygame.K_w] and self.rect1.top >= 0:
                self.move1 = -7
            if keys[pygame.K_s] and self.rect1.bottom <= 819:
                self.move1 = 7


            if keys[pygame.K_UP] and self.rect2.top >= 0:
                self.move2 = -7
            if keys[pygame.K_DOWN] and self.rect2.bottom <= 819:
                self.move2 = 7
        else:

            if keys[pygame.K_w] and self.rect1.top >= 0:
                self.move1 = -7
            if keys[pygame.K_s] and self.rect1.bottom <= 800:
                self.move1 = 7


            if keys[pygame.K_UP] and self.rect2.top >= 0:
                self.move2 = -7
            if keys[pygame.K_DOWN] and self.rect2.bottom <= 800:
                self.move2 = 7

    def destroy(self):
        if self.fullscreen:
            if self.pong.right < 0:
                self.pong = pygame.Rect(1024/2-10, 819/2, 30, 30)
                self.speed_x = random.choice([5, -5])
                self.speed_y = random.choice([4, -4])


                self.count2 += 1

            if self.pong.left > 1024:
                self.pong = pygame.Rect(1024 / 2 - 10, 819 / 2, 30, 30)
                self.speed_x = random.choice([5, -5])
                self.speed_y = random.choice([4, -4])

                self.count1 += 1

        else:
            if self.pong.right < 0:
                self.pong = pygame.Rect(380,400,30,30)
                self.speed_x = random.choice([5, -5])
                self.speed_y = random.choice([4, -4])

                self.count2 += 1
            if self.pong.left > 800:
                self.pong = pygame.Rect(380, 400, 30, 30)
                self.speed_x = random.choice([5, -5])
                self.speed_y = random.choice([4, -4])

                self.count1 += 1



    def apply_movement(self):
        if self.move1 < 0:
            self.move1 += 0.2
        if self.move1 > 0:
            self.move1 -= 0.2
        self.rect1.bottom += self.move1
        if self.fullscreen:
            if self.rect1.bottom >= 819 or self.rect1.top <= 0:
                self.move1 = 0
        else:
            if self.rect1.bottom >= 800 or self.rect1.top <= 0:
                self.move1 = 0

        if self.move2 < 0:
            self.move2 += 0.2
        if self.move2 > 0:
            self.move2 -= 0.2
        self.rect2.bottom += self.move2
        if self.fullscreen:
            if self.rect2.bottom >= 819 or self.rect2.top <= 0:
                self.move2 = 0
        else:
            if self.rect2.bottom >= 800 or self.rect2.top <= 0:
                self.move2 = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255),self.rect1)
        pygame.draw.rect(screen, (255, 255, 255), self.rect2)
        pygame.draw.rect(screen, (211,211,211), self.pong)

    def DisplayCount(self,screen):
        text_font = pygame.font.Font('Pixeled.ttf', 20)
        text_surf1 = text_font.render(str(self.count1), False, (211,211,211))

        text_surf2 = text_font.render(str(self.count2), False, (211, 211, 211))
        if self.fullscreen:
            text_rect1 = text_surf1.get_rect(topleft=((1024 / 4), 100))
            text_rect2 = text_surf2.get_rect(topleft=(int(1024-(1024/4)), 100))
        else:
            text_rect1 = text_surf1.get_rect(topleft=((800 / 4), 100))
            text_rect2 = text_surf2.get_rect(topleft=(int(800 - (800 / 4)), 100))
        screen.blit(text_surf1, text_rect1)
        screen.blit(text_surf2, text_rect2)

    def update(self, screen):
        self.movement()
        self.PongMove()
        self.apply_movement()
        self.Collision()
        self.destroy()
        self.DisplayCount(screen)
        self.draw(screen)
