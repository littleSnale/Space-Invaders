import pygame as pg


class MovingObject:
    def __init__(self, image: pg.Surface, x: int, y: int, speed: int):
        """
        Конструктор класса MovingObject
        :param image: картинка объекта
        :param x: пиксели с права
        :param y: пиксели с левого верхнего угла
        :param speed: скорость движения
        """
        self.image = image
        self.x = x
        self.y = y
        self.speed = speed
        self.fps_counter = 0

    def move(self):
        pass

    def draw(self, screen: pg.Surface):
        """
        Рисует объект на окне
        :param screen: экран
        :return: None
        """
        screen.blit(self.image, (self.x, self.y))

