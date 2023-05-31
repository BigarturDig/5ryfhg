import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Создаем поверхность пули
        self.image = pygame.Surface((self.settings.bullet_width, self.settings.bullet_height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        # Позиция пули
        self.rect.centerx = ai_game.ship.rect.centerx
        self.rect.top = ai_game.ship.rect.top

        # Сохраняем позицию пули в вещественном формате
        self.y = float(self.rect.y)

        # Определяем направление движения пули
        self.direction = 0

    def update(self):
        # Движение пули по вертикали
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

        # Движение пули по горизонтали
        if self.direction == -1:
            self.rect.x -= self.settings.bullet_speed
        elif self.direction == 1:
            self.rect.x += self.settings.bullet_speed

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)