import pygame
import random

pygame.init()

if __name__ == "__main__":
    width = 1200
    height = 920

    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Title")
    display.fill(pygame.Color("white"))
    loop = True


    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        pygame.display.update()