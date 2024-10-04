# импортируем модуль pygame как pg
import pygame as pg
# импортируем классы Player и Level
from player import Player
from level import Level


class Game:
    # создаём конструктор класса
    def __init__(self):
        """
        Конструктор класса Game
        """
        # Инициализация Pygame - подготовка pygame к программе. Нужна для работы с различными модулями Pygame
        pg.init()  # включает модуль mixer, font и другие
        # Размеры окна по пикселям
        # width - ширина окна
        self.width = 900
        # height - высота окна
        self.height = 650
        # Size - ширина и высота окна. Создаём переменную для удобства
        self.size = (self.width, self.height)
        # Задаем размеры окна
        self.screen = pg.display.set_mode(self.size)
        # Заголовок
        pg.display.set_caption('Space Invaders')
        # часы для задержки кадра
        self.clock = pg.time.Clock()
        # FPS чтобы можно было изменить
        self.fps = 60
        # переменную, которая останавливает цикл игры когда пользователь выходит
        self.running = True
        # объект класса Player
        self.player = Player(pg.image.load('images/player1.png'), 400, 530, 4, 5)
        # уровни
        self.levels = (Level('level1', 'фоновая мелодия'), Level('level1', ''))
        # текущий уровень
        self.current_level = self.levels[0]
        # звук появления щита
        self.sound_shield = pg.mixer.Sound('melodies/бонус.mp3')
        self.sound_shield.set_volume(0.1)

    # метод mainloop - это основной цикл игры, который остаётся пока переменная running - True
    def mainloop(self):
        """
        Основной цикл игры
        :return: None
        """
        # Запуск фоновой музыки
        self.current_level.start_music()
        # Запуск основного цикла
        while self.running:
            # обработка событий (handle_events - метод мой)
            self.handle_events()
            # обновление уровня
            self.current_level.update(self.player)
            if not self.player.alive:
                self.current_level.game_over.play()
                self.running = False
                # заморозить программу на время проигрыша музыки
                game_over_time = self.current_level.game_over.get_length()
                pg.time.wait(int(game_over_time * 1000))
            # рисуем окно (показываем окно)
            self.draw()
            # Обработка задержки в FPS с помощью таймера
            self.clock.tick(self.fps)

    def handle_events(self):
        """
        Обработка событий
        :return: None
        """
        # Обработка событий
        for event in pg.event.get():
            # Когда пользователь нажимает крестик, то событие регистрируется и цикл игры прекращается
            if event.type == pg.QUIT:
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    if not self.player.shield:
                        self.player.shield = True
                        self.sound_shield.play()
                    else:
                        self.player.shield = False

    def draw(self):
        """
        Рисует всё в окне
        :return: None
        """
        # Заливка экрана черным цветом
        self.screen.fill((0, 0, 0))
        # рисуем уровень
        self.current_level.draw(self.screen)
        # рисуем игрока
        self.player.draw(self.screen)
        # Обновление окна чтобы изменения стали видимыми
        pg.display.update()
