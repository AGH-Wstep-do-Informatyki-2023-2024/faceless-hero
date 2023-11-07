import pygame as pg
from entity import Entity


class Player(Entity):
    def __init__(self, groups, w, h, pos=(0, 0)):
        super(Player, self).__init__(groups, w, h, pos)

    def update(self):
        keys = pg.key.get_pressed()

        if keys[pg.K_a]:
            self.rect.x -= 10
        if keys[pg.K_d]:
            self.rect.x += 10
