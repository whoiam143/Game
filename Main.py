import pygame
import sys
import webbrowser
from Target import Target
from Button import Button


FONT_50 = pygame.font.SysFont("Montserrat", 50)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 1920
HEIGHT = 1080

FPS = 120

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))


class Main:
    def __init__(self):
        self.width = 1920
        self.height = 1080

        self.checking = {}

        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Shoot to win")
        self.display.fill(pygame.Color("black"))
        self.loop = True

        self.cursor = pygame.image.load("Texture_and_Sound/pricel.png").convert_alpha()
        pygame.mouse.set_visible(False)

        self.phon = pygame.image.load("Texture_and_Sound/Menu.png")

        self.start_butt = Button(self.width / 2 - (252 / 2), 500, 252, 75, "Start", "Texture_and_Sound/button.png",
                                  "Texture_and_Sound/button_hover.png", "Texture_and_Sound/click.mp3")
        self.authors_butt = Button(self.width / 2 - (252 / 2), 650, 252, 75, "Authors", "Texture_and_Sound/button.png",
                                    "Texture_and_Sound/button_hover.png", "Texture_and_Sound/click.mp3")
        self.exit_butt = Button(self.width / 2 - (252 / 2), 800, 252, 75, "Exit", "Texture_and_Sound/button.png",
                                 "Texture_and_Sound/button_hover.png", "Texture_and_Sound/click.mp3")

        self.level1 = Button(600, 420, 150, 150, "1", "Texture_and_Sound/level_button.png",
                                 "Texture_and_Sound/level_button_hover.png", "Texture_and_Sound/click.mp3")
        self.level2 = Button(900, 420, 150, 150, "2", "Texture_and_Sound/level_button.png",
                             "Texture_and_Sound/level_button_hover.png", "Texture_and_Sound/click.mp3")
        self.level3 = Button(1200, 420, 150, 150, "3", "Texture_and_Sound/level_button.png",
                             "Texture_and_Sound/level_button_hover.png", "Texture_and_Sound/click.mp3")
        self.level4 = Button(750, 650, 150, 150, "4", "Texture_and_Sound/level_button.png",
                             "Texture_and_Sound/level_button_hover.png", "Texture_and_Sound/click.mp3")
        self.level5 = Button(1050, 650, 150, 150, "5", "Texture_and_Sound/level_button.png",
                             "Texture_and_Sound/level_button_hover.png", "Texture_and_Sound/click.mp3")


    def show_authours(self):  # Окно авторов
        loop = True
        self.display.fill((255, 255, 255))

        link_color1 = (0, 0, 0)
        link_color2 = (0, 0, 0)

        Emil = FONT_50.render("Cултанов Эмиль", True, BLACK)
        Adil = FONT_50.render("Ахметов Адиль", True, BLACK)

        #self.display.blit(self.phon, [0, 0])
        while loop:
            self.display.blit(self.phon, [0, 0])

            self.display.blit(Emil, (600, 500))
            self.display.blit(Adil, (1100, 500))

            git1 = self.display.blit(FONT_50.render("Github", True, link_color1), (680, 600))
            git2 = self.display.blit(FONT_50.render("Github", True, link_color2), (1180, 600))

            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.display.blit(self.cursor, pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # Возврат в меню при нажатие на esc
                    if event.key == pygame.K_ESCAPE:
                        loop = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = event.pos

                    if git1.collidepoint(pos):
                        webbrowser.open(r"https://github.com/whoiam143")

                    if git2.collidepoint(pos):
                        webbrowser.open(r"https://github.com/zetistheself")

            # Если наводить меняется цвет
            if git1.collidepoint(pygame.mouse.get_pos()):
                link_color1 = (70, 30, 220)
            else:
                link_color1 = (0, 0, 0)

            if git2.collidepoint(pygame.mouse.get_pos()):
                link_color2 = (70, 30, 220)
            else:
                link_color2 = (0, 0, 0)

            pygame.display.update()
            pygame.display.flip()

    def main_game_loop(self):
        while self.loop:
            self.display.blit(self.phon, [0, 0])

            self.start_butt.draw_button(self.display)
            self.start_butt.check_hover(pygame.mouse.get_pos())
            self.authors_butt.draw_button(self.display)
            self.authors_butt.check_hover(pygame.mouse.get_pos())
            self.exit_butt.draw_button(self.display)
            self.exit_butt.check_hover(pygame.mouse.get_pos())

            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.display.blit(self.cursor, pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.USEREVENT and event.button == self.exit_butt):
                    self.loop = False
                    sys.exit()
                if event.type == pygame.USEREVENT and event.button == self.authors_butt:
                    self.show_authours()
                if event.type == pygame.USEREVENT and event.button == self.start_butt:
                    self.menu_of_levels()

                self.start_butt.handle_event(event)
                self.authors_butt.handle_event(event)
                self.exit_butt.handle_event(event)

            pygame.display.flip()

    def menu_of_levels(self):
        loop = True
        self.display.fill((255, 255, 255))

        while loop:
            self.display.blit(self.phon, [0, 0])

            self.level1.draw_button(self.display)
            self.level1.check_hover(pygame.mouse.get_pos())

            self.level2.draw_button(self.display)
            self.level2.check_hover(pygame.mouse.get_pos())

            self.level3.draw_button(self.display)
            self.level3.check_hover(pygame.mouse.get_pos())

            self.level4.draw_button(self.display)
            self.level4.check_hover(pygame.mouse.get_pos())

            self.level5.draw_button(self.display)
            self.level5.check_hover(pygame.mouse.get_pos())

            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.display.blit(self.cursor, pos)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # Возврат в меню при нажатие на esc
                    if event.key == pygame.K_ESCAPE:
                        loop = False
                if event.type == pygame.USEREVENT and event.button == self.level1:
                    self.game_1()

                self.level1.handle_event(event)
                self.level2.handle_event(event)
                self.level3.handle_event(event)
                self.level4.handle_event(event)
                self.level5.handle_event(event)

            pygame.display.update()
            pygame.display.flip()

    def game_1(self):
        loop = True
        clock = pygame.time.Clock()
        sound_path = 'Texture_and_Sound/shoot.mp3'
        self.sound = pygame.mixer.Sound(sound_path)
        self.display.fill((0, 0, 0))
        shoot_image = pygame.image.load("Texture_and_Sound/shoot.png").convert_alpha()
        background = pygame.image.load('Texture_and_Sound/level1.png').convert_alpha()
        self.display.blit(background, [0, 0])
        background = pygame.transform.scale(background, (WIDTH, HEIGHT))
        all_sprites = pygame.sprite.Group()
        all_sprites.draw(self.display)
        for i in range(3):
            Target(all_sprites)
        all_sprites.draw(self.display)

        while loop:
            clock.tick(FPS)
            shoot = pygame.sprite.Sprite(all_sprites)
            shoot.image = shoot_image
            shoot.rect = shoot.image.get_rect()
            shoot.rect.x = 1382
            shoot.rect.y = 647
            shoot.kill()
            pos = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.display.blit(self.cursor, pos)
            pygame.display.flip()
            background = pygame.image.load('Texture_and_Sound/level1.png')
            self.display.blit(background, [0, 0])
            background = pygame.transform.scale(background, (self.width, self.height))
            all_sprites.draw(self.display)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # Возврат в меню при нажатие на esc
                    if event.key == pygame.K_ESCAPE:
                        loop = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for bomb in all_sprites:
                        all_sprites.update(event)
                    shoot = pygame.sprite.Sprite(all_sprites)
                    shoot.image = shoot_image
                    shoot.rect = shoot.image.get_rect()
                    shoot.rect.x = 1350
                    shoot.rect.y = 630
                    self.sound.play()
                    all_sprites.draw(self.display)
                if event.type == pygame.MOUSEMOTION:
                    pos = pygame.mouse.get_pos()
                    if pygame.mouse.get_focused():
                        self.display.blit(self.cursor, pos)
                shoot.kill()
            clock.tick(FPS)


        def game_2(self):
            loop = True
            clock = pygame.time.Clock()
            sound_path = 'Texture_and_Sound/shoot.mp3'
            self.sound = pygame.mixer.Sound(sound_path)
            self.display.fill((0, 0, 0))
            shoot_image = pygame.image.load("Texture_and_Sound/shoot.png").convert_alpha()
            background = pygame.image.load('Texture_and_Sound/Phon.png').convert_alpha()
            self.display.blit(background, [0, 0])
            background = pygame.transform.scale(background, (WIDTH, HEIGHT))
            all_sprites = pygame.sprite.Group()
            all_sprites.draw(self.display)
            for i in range(3):
                Target(all_sprites)
            all_sprites.draw(self.display)

            while loop:
                clock.tick(FPS)
                shoot = pygame.sprite.Sprite(all_sprites)
                shoot.image = shoot_image
                shoot.rect = shoot.image.get_rect()
                shoot.rect.x = 1382
                shoot.rect.y = 647
                shoot.kill()
                pos = pygame.mouse.get_pos()
                if pygame.mouse.get_focused():
                    self.display.blit(self.cursor, pos)
                pygame.display.flip()
                background = pygame.image.load('Texture_and_Sound/Phon.png')
                self.display.blit(background, [0, 0])
                background = pygame.transform.scale(background, (self.width, self.height))
                all_sprites.draw(self.display)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        loop = False
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        # Возврат в меню при нажатие на esc
                        if event.key == pygame.K_ESCAPE:
                            loop = False

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        for bomb in all_sprites:
                            all_sprites.update(event)
                        shoot = pygame.sprite.Sprite(all_sprites)
                        shoot.image = shoot_image
                        shoot.rect = shoot.image.get_rect()
                        shoot.rect.x = 1350
                        shoot.rect.y = 630
                        self.sound.play()
                        all_sprites.draw(self.display)
                    if event.type == pygame.MOUSEMOTION:
                        pos = pygame.mouse.get_pos()
                        if pygame.mouse.get_focused():
                            self.display.blit(self.cursor, pos)
                    shoot.kill()
                clock.tick(FPS)

if __name__ == "__main__":
    game = Main()
    game.main_game_loop()