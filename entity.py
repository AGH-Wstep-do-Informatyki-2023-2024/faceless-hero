import pygame as pg


# Implements basic movement physics
class Entity(pg.sprite.Sprite):
    def __init__(self, groups, w, h, pos=(0, 0)):
        super(Entity, self).__init__(groups)

        self.image = pg.Surface((w, h))
        self.rect = self.image.get_rect(topleft=pos)

        self.vx = 0
        self.vy = 0
        self.mass = 0
