import pygame


FONT_50 = pygame.font.SysFont("Montserrat", 50)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


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
