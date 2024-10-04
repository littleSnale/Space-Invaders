from random import randint

import pygame as pg

size = (500, 500)
screen = pg.display.set_mode(size)

fps = 10

clock = pg.time.Clock()

while True:
    screen.fill(pg.Color('white'))

    type_ = randint(0, 3)

    if type_ == 0:
        pg.draw.circle(screen, pg.Color('red'), (100, 100), 50)
    if type_ == 1:
        pg.draw.rect(screen, pg.Color('blue'), (200, 300, 70, 100))
    if type_ == 2:
        pg.draw.ellipse(screen, pg.Color('green'), (178, 20, 70, 100))
    if type_ == 3:

        pg.draw.polygon(screen, pg.Color('black'), (150, 170), (450, 70))

    pg.display.flip()
    clock.tick(fps)
