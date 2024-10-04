from movingobjects import MovingObject
from bullet import Bullet
import random
import pygame as pg


class Enemy(MovingObject):
    def __init__(self, image: pg.Surface, x: int, y: int, speed: int, hp: int):
        # вызываем инит класса MovingObject
        MovingObject.__init__(self, image, x, y, speed)
        self.hp = hp
        self.fps_counter = random.randint(0, 59)

    # решение через точки
    def is_hit(self, bullet: Bullet) -> bool:
        bullet_bottom = bullet.y + bullet.image.get_height()
        bullet_right = bullet.x + bullet.image.get_width()
        self_bottom = self.y + self.image.get_height()
        self_right = self.x + self.image.get_width()
        if bullet.x > self.x and bullet_bottom < self_bottom and bullet_right < self_right and bullet.y > self.y:
            return True
        else:
            return False

    def move(self):
        """
        Передвижение врагов
        :return: None
        """

        if self.fps_counter % 10 == 0:
            self.y += self.speed
            if random.randint(1, 2) == 1:
                if self.x > 0:
                    self.x -= self.speed
            else:
                if self.x + self.image.get_width() < 900:
                    self.x += self.speed
