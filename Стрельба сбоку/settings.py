class Settings:
    def __init__(self):
        """Инициализирует атрибуты"""
        self.screen_width = 1200  # Инициализирует ширину экрана
        self.screen_height = 800  # Инициализирует высоту экрана
        self.bg_color = (0, 32, 255)  # Инициализирует цвет заднего фона

        self.bullet_width = 3  # Ширина пули
        self.bullet_height = 15  # Высота пули
        self.bullet_color = (60, 60, 60)  # Цвет пули
        self.bullets_allowed = 3  # Максимальная очередь
        self.bullet_speed = 6.0  # Скорость пули

        self.ship_speed = 1.5  # Скорость корабля