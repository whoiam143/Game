import pygame
import sys
import webbrowser
import random
import time

from db import add_result, results, create_bd

WIDTH = 1920
HEIGHT = 1080

pygame.init()
window = pygame.display.set_mode((WIDTH, HEIGHT))

FONT_50 = pygame.font.SysFont("Montserrat", 50)
FONT_100 = pygame.font.SysFont("Montserrat", 100)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

FPS = 120

hits_count = 0
shoot_count = 0


class Button:
    def __init__(self, x, y, width, height, text, image_path, hover_impage_path=None, sound_path=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

        self._image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self._image, (width, height))
        self.hover_image = self.image
        if hover_impage_path:
            self.hover_image = pygame.image.load(hover_impage_path)
            self.hover_image = pygame.transform.scale(self.hover_image, (width, height))

        self.rect = self.image.get_rect(topleft=(x, y))
        self.sound = None
        if sound_path:
            self.sound = pygame.mixer.Sound(sound_path)

        self.is_hovered = False

    def draw_button(self, screen):  # Метод нарисовки кнопки
        if self.is_hovered:
            current_image = self.hover_image
        else:
            current_image = self.image
        screen.blit(current_image, self.rect.topleft)

        text_surface = FONT_50.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_hover(self, mouse_pos):  # Проверка ли мышь на кнопке
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):  # Звук при нажатие на кнопку
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.sound:
                self.sound.play()
            pygame.event.post(pygame.event.Event(pygame.USEREVENT, button=self))


class Main:
    def __init__(self):
        global hits_count
        self.width = 1920
        self.height = 1080

        self.checking = {}

        self.display = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Shoot to win")
        self.display.fill(pygame.Color("black"))
        self.loop = True

        self.cursor = pygame.image.load("Texture_and_Sound/pricel.png").convert_alpha()
        pygame.mouse.set_visible(False)

        self.sec = 0
        self.minut = 0

        self.time = ''
        create_bd()

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

            x,y = pygame.mouse.get_pos()
            pos = x - 25, y - 25
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
    
    def timer(self, start_time):
        #print(start_time)
        current_time = int(time.time() - start_time)
        self.sec = current_time
        if current_time >= 60:
            self.sec = 0
            start_time += current_time
            self.minut += 1
            current_time = 0
            
        if self.sec < 10:
            if self.minut < 10:
                self.time = current_time = f"0{self.minut}:0{self.sec}"
            else:
                self.time = current_time = f"{self.minut}:0{self.sec}"
        if self.sec >= 10:
            if self.minut < 10:
                self.time = current_time = f"0{self.minut}:{self.sec}"
            else:
                self.time = current_time = f"{self.minut}:{self.sec}"

        self.display.blit(FONT_50.render(current_time, True, WHITE), (0, 100))
        return start_time


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

            x, y = pygame.mouse.get_pos()
            pos = x - 25, y - 25
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

    def save_results(self, level):
        accuracy = 0
        global shoot_count
        try:
            accuracy = int(round(hits_count / (shoot_count / 3), 2) * 100)
        except ZeroDivisionError:
            pass
        if accuracy > 100:
            accuracy = 100
        add_result(self.time, level, hits_count, f'{accuracy}%')

    def show_results(self):
        global hits_count

        loop = True
        self.display.fill((255, 255, 255))

        link_color1 = (0, 0, 0)

        accuracy = int(round(hits_count / (shoot_count / 3), 2) * 100)
        if accuracy > 100:
            accuracy = 100

        phon = pygame.image.load("Texture_and_Sound/Menu.png").convert_alpha()

        while loop:
            self.display.blit(phon, [0, 0])

            self.display.blit(FONT_100.render(f"Score:{hits_count}", True, link_color1), (850, 450))
            self.display.blit(FONT_50.render(f"Time:{self.time}", True, link_color1), (880, 545))
            self.display.blit(FONT_50.render(f"Accuracy:{accuracy}%", True, link_color1), (850, 605))

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
            
            pygame.display.flip()
        
        hits_count = 0

    def game_1(self):
        global shoot_count
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
        start_time = time.time()
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
            start_time = self.timer(start_time)
            x, y = pygame.mouse.get_pos()
            if pygame.mouse.get_focused():
                self.display.blit(self.cursor, (x - 25, y - 25))
            pygame.display.flip()
            background = pygame.image.load('Texture_and_Sound/level1.png')
            self.display.blit(background, [0, 0])
            background = pygame.transform.scale(background, (self.width, self.height))
            all_sprites.draw(self.display)
            self.display.blit(FONT_50.render(f"Hits:{hits_count}", True, WHITE), (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    loop = False
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    # Возврат в меню при нажатие на esc
                    if event.key == pygame.K_ESCAPE:
                        loop = False
                        self.save_results(1)
                        self.show_results()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    for bomb in all_sprites:
                        all_sprites.update(event)
                        shoot_count += 1
                    shoot = pygame.sprite.Sprite(all_sprites)
                    shoot.image = shoot_image
                    shoot.rect = shoot.image.get_rect()
                    shoot.rect.x = 1350
                    shoot.rect.y = 630
                    self.sound.play()
                    all_sprites.draw(self.display)
                if event.type == pygame.MOUSEMOTION:
                    x, y = pygame.mouse.get_pos()
                    if pygame.mouse.get_focused():
                        self.display.blit(self.cursor, (x - 25, y - 25))
                shoot.kill()
            clock.tick(FPS)
        pygame.display.flip()


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


class Target(pygame.sprite.Sprite):
    image = pygame.image.load("Texture_and_Sound/target.png").convert_alpha()

    def __init__(self, group):
        super().__init__(group)
        self.group = group
        self.image = Target.image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(400, 400 + 1000 - 100)
        self.rect.y = random.randrange(172, 720 + 172 - 100)

    def update(self, *args):
        global hits_count
        if args and args[0].type == pygame.MOUSEBUTTONDOWN and \
                self.rect.collidepoint(args[0].pos):
            self.kill()
            hits_count += 1
            print(hits_count)
            Target(self.group)


if __name__ == "__main__":
    game = Main()
    game.main_game_loop()