from movingobjects import MovingObject
import pygame as pg
from bullet import Bullet


class Player(MovingObject):
    def __init__(self, image: pg.Surface, x: int, y: int, speed: int, hp: int):
        # вызываем инит класса MovingObject
        MovingObject.__init__(self, image, x, y, speed)
        self.hp = hp
        self.body = pg.Rect(self.x + self.image.get_width() // 3, self.y, self.image.get_width() // 3,
                            self.image.get_height())
        self.wings = pg.Rect(self.x, self.y + self.image.get_height() - self.image.get_height() // 3,
                             self.image.get_width(),
                             self.image.get_height() // 3)
        self.alive = True
        self.shield = False

    def is_hit(self, bullet: Bullet) -> bool:
        # если пуля касается прямоугольников, то возвращаем True
        bullet_bottom = bullet.y + bullet.image.get_height()
        bullet_right = bullet.x + bullet.image.get_width()
        if bullet.x > self.body.left and bullet_bottom < self.body.bottom \
                and bullet_right < self.body.right and bullet.y > self.body.top or bullet.x > self.wings.left \
                and bullet_bottom < self.wings.bottom \
                and bullet_right < self.wings.right and bullet.y > self.wings.top:
            return True
        else:
            return False

    def draw(self, screen: pg.Surface):
        """
        Рисует объект на окне
        :param screen: экран
        :return: None
        """
        screen.blit(self.image, (self.x, self.y))
        if self.shield:
            pg.draw.rect(screen, 'green', self.body, 5)
            pg.draw.rect(screen, 'orange ', self.wings, 5)

    def move(self):
        """
        Движение игрока
        :return: None
        """
        pressed_keys = pg.key.get_pressed()
        if self.y > 0:
            if pressed_keys[pg.K_w] or pressed_keys[pg.K_UP]:
                self.y -= self.speed
                if self.y < 0:
                    self.y = 0
        if self.y < 555:
            if pressed_keys[pg.K_s] or pressed_keys[pg.K_DOWN]:
                self.y += self.speed
                if self.y > 555:
                    self.y = 555
        if self.x > 0:
            if pressed_keys[pg.K_a] or pressed_keys[pg.K_LEFT]:
                self.x -= self.speed
                if self.x < 0:
                    self.x = 0
        if self.x < 800:
            if pressed_keys[pg.K_d] or pressed_keys[pg.K_RIGHT]:
                self.x += self.speed
                if self.x > 800:
                    self.x = 800
        self.body.x = self.x + self.image.get_width() // 3
        self.body.y = self.y
        self.wings.x = self.x
        self.wings.y = self.y + self.image.get_height() - self.image.get_height() // 3
