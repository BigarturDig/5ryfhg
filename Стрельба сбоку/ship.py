import pygame  # импортируем модуль pygame


class Ship:
    """создаем класс Корабль"""

    def __init__(self, ai_game):
        """создаем метод-конструктор класса"""
        self.screen = ai_game.screen  # присваиваем переменной screen значение аргумента ai_game.screen
        self.settings = ai_game.settings  # присваиваем переменной settings значение аргумента ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()  # присваиваем переменной screen_rect прямоугольник экрана
        self.image = pygame.image.load('images/ship.bmp')  # загружаем изображение корабля и присваиваем его переменной image
        self.rect = self.image.get_rect()  # присваиваем переменной rect прямоугольник корабля
        self.rect.midbottom = self.screen_rect.midbottom  # задаем позицию корабля на экране
        self.x = float(self.rect.x)  # записываем координату x корабля в отдельную переменную
        self.y = float(self.rect.y)  # записываем координату y корабля в отдельную переменную
        self.moving_right = False  # флаг движения вправо не поднят
        self.moving_left = False  # флаг движения влево не поднят
        self.moving_up = False  # флаг движения вверх не поднят
        self.moving_down = False  # флаг движения вниз не поднят

    def update(self):
        """метод, обновляющий позицию корабля на экране"""
        if self.moving_right and self.rect.right < self.screen_rect.right:  # если флаг движения вправо поднят и не дошли до правой границы экрана
            self.x += self.settings.ship_speed  # увеличиваем координату x корабля
        if self.moving_left and self.rect.left > 0:  # если флаг движения влево поднят и не дошли до левой границы экрана
            self.x -= self.settings.ship_speed  # уменьшаем координату x корабля
        if self.moving_up and self.rect.top > self.screen_rect.top:  # если флаг движения вверх поднят и не дошли до верхней границы экрана
            self.y -= self.settings.ship_speed  # уменьшаем координату y корабля
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:  # если флаг движения вниз поднят и не дошли до нижней границы экрана
            self.y += self.settings.ship_speed  # увеличиваем координату y корабля
        self.rect.x = self.x  # обновляем координату x прямоугольника корабля
        self.rect.y = self.y  # обновляем координату y прямоугольника корабля

    def blitme(self):  # метод, выводящий корабль на экран
        self.screen.blit(self.image, self.rect)  # выводим изображение корабля в прямоугольнике rect на экране