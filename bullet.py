from movingobjects import MovingObject
import pygame as pg


class Bullet(MovingObject):
    def __init__(self, image: pg.Surface, x: int, y: int, speed: int, direction: str):
        """
        Конструктор класса Bullet
        :param image: картинка
        :param x: x
        :param y: y
        :param speed: скорость передвижения
        :param direction: направление
        """
        # вызываем инит класса MovingObject
        MovingObject.__init__(self, image, x, y, speed)
        self.direction = direction

    def move(self):
        """
        Передвижение пули
        :return: None.
        """
        if self.direction == 'up':
            self.y -= self.speed
        else:
            self.y += self.speed
