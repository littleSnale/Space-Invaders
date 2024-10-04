import pygame as pg
from enemy import Enemy
from bullet import Bullet
from player import Player
import random


class Level:
    def __init__(self, background_name: str, music_name: str):
        """
        Конструктор класса Level
        :param background_name: фон
        :param music_name: музыка
        """
        self.background = pg.image.load(f'images/{background_name}.jpg')
        self.music = f'melodies/{music_name}.mp3'
        self.enemies = self.create_enemies()
        self.bullets = []
        self.bullet_image = pg.image.load('images/пуля.png')
        self.enemy_bullet_image = pg.image.load('images/пуля2.png')
        # звук вылета пули
        self.sound_bullet = pg.mixer.Sound('melodies/звук выстрела.mp3')
        self.sound_bullet.set_volume(0.1)
        # звук поражения
        self.game_over = pg.mixer.Sound('melodies/звук поражения.mp3')
        self.game_over.set_volume(0.1)

    @staticmethod
    def create_enemies() -> list[Enemy]:
        """
        Создаём врагов
        :return: список[врагов]
        """
        shift_x = 150
        shift_y = 80
        start_x = 25
        start_y = -200
        enemies = []
        for j in range(5):
            for i in range(6):
                enemies.append(Enemy(pg.image.load('images/enemy1.png'),
                                     i * shift_x + start_x, j * shift_y + start_y, 1, 3))
        return enemies

    def start_music(self):
        """
        Добавляет музыку в уровень
        :return: None
        """
        pg.mixer.music.load(self.music)
        pg.mixer.music.set_volume(0.1)
        pg.mixer.music.play(1)

    def update(self, player: Player):
        """
        Рисует всё, в уровне 1
        :param player: игрок
        :return: None
        """
        self.handle_hits(player)
        for enemy in self.enemies:
            enemy.move()
            enemy.fps_counter += 1
            if enemy.y + enemy.image.get_height() >= 650:
                player.alive = False
            if enemy.fps_counter == 60:
                if random.randint(1, 100) <= 10:
                    enemy_bullet_x = enemy.x + enemy.image.get_width() / 2 - self.enemy_bullet_image.get_width() / 2
                    self.bullets.append(Bullet(self.enemy_bullet_image, enemy_bullet_x,
                                               enemy.y + enemy.image.get_height(), 1, 'down'))
                    self.sound_bullet.play()
                enemy.fps_counter = 0

        for bullet in self.bullets:
            # избавиться от утечки памяти
            if bullet.y > 900 or bullet.y < 0 - bullet.image.get_height():
                self.bullets.remove(bullet)

            bullet.move()
        # движение игрока
        player.move()
        # появление пули
        player.fps_counter += 1
        if player.fps_counter == 35:
            bullet_x = player.x + player.image.get_width() / 2 - self.bullet_image.get_width() / 2
            self.bullets.append(Bullet(self.bullet_image, bullet_x, player.y, 5, 'up'))
            player.fps_counter = 0

    def handle_hits(self, player: Player):
        for bullet in self.bullets:
            if bullet.direction == 'up':
                # Пробежаться по всем врагам. Если пуля попала - уменьшать hp врага. Если hp == 0, то удалять врага

                for enemy in self.enemies:
                    if enemy.is_hit(bullet):
                        enemy.hp -= 1
                        self.bullets.remove(bullet)
                        if enemy.hp <= 0:
                            self.enemies.remove(enemy)
                        break
            else:
                # Если пуля попала уменьшать hp игрока. Добавить метод is_hit. Если hp = 0, то заменить картинку игрока.
                if not player.shield:
                    if player.is_hit(bullet) and bullet.direction == 'down':
                        player.hp -= 1
                        self.bullets.remove(bullet)
                        if player.hp <= 0 and player.alive:
                            player.alive = False

    def draw(self, screen: pg.Surface):
        """
        Рисует весь уровень
        :param screen: экран
        :return: None
        """
        # рисуется фон
        screen.blit(self.background, (0, 0))
        # рисуем пули
        for bullet in self.bullets:
            bullet.draw(screen)
        # рисуем врагов
        for enemy in self.enemies:
            enemy.draw(screen)
