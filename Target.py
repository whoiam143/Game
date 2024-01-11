import pygame
from random import randrange


class Target(pygame.sprite.Sprite):
    image = pygame.image.load("Texture_and_Sound/target.png").convert_alpha()

    def __init__(self, group):
        super().__init__(group)
        self.group = group
        self.image = Target.image
        self.rect = self.image.get_rect()
        self.rect.x = randrange(400, 400 + 1000 - 100)
        self.rect.y = randrange(172, 720 + 172 - 100)

    def update(self, *args):
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.kill()
            Target(self.group)