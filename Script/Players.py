import pygame


class Players(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        if player == '1':
            self.rect = pygame.Rect(50,350, 20,150)
        elif player == '2':
            self.rect = pygame.Rect(730,350, 20,150)
        self.mode = player
        self.move = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if self.mode == '1':
            if keys[pygame.K_w] and self.rect.top >= 0:
                self.move = -7
            if keys[pygame.K_s] and self.rect.bottom <= 800:
                self.move = 7

        if self.mode == '2':
            if keys[pygame.K_UP] and self.rect.top >= 0:
                self.move = -7
            if keys[pygame.K_DOWN] and self.rect.bottom <= 800:
                self.move = 7


    def apply_movement(self):
        if self.move < 0:
            self.move += 0.2
        if self.move > 0:
            self.move -= 0.2
        self.rect.bottom += self.move
        if self.rect.bottom >= 800 or self.rect.top <= 0:
            self.move = 0

    def draw(self, screen):
        pygame.draw.rect(screen, (255,255,255),self.rect)

    def update(self, screen):
        self.movement()
        self.apply_movement()
        self.draw(screen)